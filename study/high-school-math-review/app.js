const TEXT_PREVIEW_LIMIT = 512 * 1024;
const LIST_PAGE_SIZE = 160;

const GROUPS = {
  all: { label: "全部", extensions: null },
  notes: { label: "笔记", extensions: new Set(["md", "txt", "url", ""]) },
  images: { label: "图片", extensions: new Set(["png", "jpg", "jpeg", "webp", "gif", "svg"]) },
  data: { label: "数据", extensions: new Set(["json", "csv"]) },
  code: { label: "脚本", extensions: new Set(["py", "ps1", "js", "ts", "css", "html", "htm"]) },
  files: { label: "文档", extensions: new Set(["docx", "zip", "pptx", "xlsx", "pdf"]) }
};

const QUICK_LINKS = [
  ["学习工作台", "学习工作台.md"],
  ["互动工作台", "学习工作台.html"],
  ["LLM Wiki", "LLM知识库/wiki/00_Index.md"],
  ["二轮题库", "Obsidian题库/README.md"],
  ["五年经典", "高考数学五年经典/README.md"],
  ["个人错题库", "个人错题库/README.md"],
  ["AI 笔记", "Obsidian题库/08_AI笔记管理/AI学习流水线.md"],
  ["大文件清单", "未上传大文件清单.md"]
];

const state = {
  files: [],
  byPath: new Map(),
  lookup: new Map(),
  counts: {},
  activePath: "",
  query: "",
  group: "all",
  visibleLimit: LIST_PAGE_SIZE,
  openRequestId: 0
};

const elements = {
  search: document.getElementById("search"),
  quickLinks: document.getElementById("quick-links"),
  typeFilters: document.getElementById("type-filters"),
  fileList: document.getElementById("file-list"),
  resultCount: document.getElementById("result-count"),
  libraryStats: document.getElementById("library-stats"),
  fileTitle: document.getElementById("file-title"),
  fileMeta: document.getElementById("file-meta"),
  rawLink: document.getElementById("raw-link"),
  content: document.getElementById("content"),
  toc: document.getElementById("toc")
};

if (window.marked) {
  marked.setOptions({
    breaks: true,
    gfm: true
  });
}

function normalize(text = "") {
  return String(text).toLowerCase().trim();
}

function normalizeLookup(text = "") {
  return normalize(text)
    .replace(/\\/g, "/")
    .replace(/\.(md|txt|html|htm|json|csv|png|jpe?g|webp|gif|svg|docx|zip)$/i, "")
    .replace(/^\.?\//, "");
}

function encodePath(path) {
  return path
    .split("/")
    .map((part) => encodeURIComponent(part))
    .join("/");
}

function fileUrl(path) {
  return `./files/${encodePath(path)}`;
}

function displaySize(bytes = 0) {
  if (bytes < 1024) {
    return `${bytes} B`;
  }
  if (bytes < 1024 * 1024) {
    return `${(bytes / 1024).toFixed(1)} KB`;
  }
  return `${(bytes / 1024 / 1024).toFixed(2)} MB`;
}

function extOf(path = "") {
  const match = path.match(/\.([^.\/]+)$/);
  return match ? match[1].toLowerCase() : "";
}

function basename(path = "") {
  const index = path.lastIndexOf("/");
  return index >= 0 ? path.slice(index + 1) : path;
}

function dirname(path = "") {
  const index = path.lastIndexOf("/");
  return index >= 0 ? path.slice(0, index) : "";
}

function stripExtension(name = "") {
  return name.replace(/\.[^.\/]+$/, "");
}

function normalizePath(path = "") {
  const parts = [];
  path.replace(/\\/g, "/").split("/").forEach((part) => {
    if (!part || part === ".") {
      return;
    }
    if (part === "..") {
      parts.pop();
      return;
    }
    parts.push(part);
  });
  return parts.join("/");
}

function groupForExt(ext) {
  if (GROUPS.images.extensions.has(ext)) {
    return "images";
  }
  if (GROUPS.data.extensions.has(ext)) {
    return "data";
  }
  if (GROUPS.code.extensions.has(ext)) {
    return "code";
  }
  if (GROUPS.files.extensions.has(ext)) {
    return "files";
  }
  return "notes";
}

function addLookup(key, path) {
  const normalized = normalizeLookup(key);
  if (!normalized) {
    return;
  }
  const matches = state.lookup.get(normalized) || [];
  if (!matches.includes(path)) {
    matches.push(path);
    state.lookup.set(normalized, matches);
  }
}

function buildIndexes() {
  state.lookup.clear();
  state.counts = Object.fromEntries(Object.keys(GROUPS).map((key) => [key, 0]));
  state.counts.all = state.files.length;

  state.files.forEach((file) => {
    const path = normalizePath(file.path);
    const ext = extOf(path);
    const group = groupForExt(ext);
    state.counts[group] = (state.counts[group] || 0) + 1;

    addLookup(path, path);
    addLookup(stripExtension(path), path);
    addLookup(basename(path), path);
    addLookup(stripExtension(basename(path)), path);
    addLookup(file.title, path);
  });
}

function bestCandidate(candidates, basePath) {
  if (!candidates?.length) {
    return "";
  }
  const baseDir = dirname(basePath);
  const sameDir = candidates.find((path) => dirname(path) === baseDir);
  if (sameDir) {
    return sameDir;
  }
  const markdown = candidates.find((path) => extOf(path) === "md");
  return markdown || candidates[0];
}

function findFileByReference(reference, basePath = "") {
  if (!reference) {
    return "";
  }

  const decoded = safeDecode(reference).replace(/^\.?\//, "");
  const normalized = normalizePath(decoded);
  const baseDir = dirname(basePath);
  const vaultRoot = basePath.includes("/") ? basePath.split("/")[0] : "";
  const candidates = [
    normalized,
    normalizePath(`${baseDir}/${decoded}`),
    vaultRoot ? normalizePath(`${vaultRoot}/${decoded}`) : "",
    `${normalized}.md`,
    normalizePath(`${baseDir}/${decoded}.md`),
    vaultRoot ? normalizePath(`${vaultRoot}/${decoded}.md`) : ""
  ].filter(Boolean);

  for (const candidate of candidates) {
    if (state.byPath.has(candidate)) {
      return candidate;
    }
  }

  const lookupCandidates =
    state.lookup.get(normalizeLookup(normalized)) ||
    state.lookup.get(normalizeLookup(basename(normalized))) ||
    [];
  return bestCandidate(lookupCandidates, basePath);
}

function safeDecode(value) {
  try {
    return decodeURIComponent(value);
  } catch {
    return value;
  }
}

function splitHref(href = "") {
  const hashIndex = href.indexOf("#");
  const beforeHash = hashIndex >= 0 ? href.slice(0, hashIndex) : href;
  const hash = hashIndex >= 0 ? safeDecode(href.slice(hashIndex + 1)) : "";
  const queryIndex = beforeHash.indexOf("?");
  const cleanPath = queryIndex >= 0 ? beforeHash.slice(0, queryIndex) : beforeHash;
  return { cleanPath, hash };
}

function resolveRelative(basePath, href) {
  const { cleanPath, hash } = splitHref(href);
  if (!cleanPath) {
    return { path: "", hash, samePage: true };
  }
  if (/^[a-z]+:/i.test(cleanPath) || cleanPath.startsWith("/")) {
    return { path: cleanPath, hash, external: true };
  }
  const found = findFileByReference(cleanPath, basePath);
  return { path: found, hash, external: false };
}

function pathFromRoute() {
  const params = new URLSearchParams(window.location.hash.slice(1));
  return params.get("file") || "";
}

function anchorFromRoute() {
  const params = new URLSearchParams(window.location.hash.slice(1));
  return params.get("anchor") || "";
}

function setRoute(path, anchor = "") {
  const params = new URLSearchParams();
  params.set("file", path);
  if (anchor) {
    params.set("anchor", anchor);
  }
  const nextHash = `#${params.toString()}`;
  if (window.location.hash !== nextHash) {
    window.location.hash = nextHash;
  } else {
    openFile(path, anchor);
  }
}

function escapeHtml(text = "") {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function escapeMarkdownLabel(text = "") {
  return String(text).replace(/([\\\[\]])/g, "\\$1");
}

function renderInlineFallback(text = "") {
  const placeholders = [];
  const hold = (html) => {
    const token = `@@MDTOKEN${placeholders.length}@@`;
    placeholders.push([token, html]);
    return token;
  };

  let source = String(text)
    .replace(/<span class="local-file-link">([\s\S]*?)<\/span>/g, (_, label) =>
      hold(`<span class="local-file-link">${escapeHtml(label)}</span>`)
    )
    .replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (_, alt, href) =>
      hold(`<img src="${escapeHtml(href)}" alt="${escapeHtml(alt)}" loading="lazy">`)
    )
    .replace(/\[([^\]]+)\]\(<file:[^)]+>\)/gi, (_, label) =>
      hold(`<span class="local-file-link">${escapeHtml(label)}</span>`)
    )
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) =>
      hold(`<a href="${escapeHtml(href)}">${escapeHtml(label)}</a>`)
    )
    .replace(/`([^`]+)`/g, (_, code) => hold(`<code>${escapeHtml(code)}</code>`));

  source = escapeHtml(source);
  placeholders.forEach(([token, html]) => {
    source = source.replaceAll(token, html);
  });
  return source;
}

function basicMarkdownToHtml(markdown = "") {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const html = [];
  let paragraph = [];
  let list = [];
  let quote = [];
  let code = [];
  let inCode = false;

  const flushParagraph = () => {
    if (!paragraph.length) {
      return;
    }
    html.push(`<p>${paragraph.map(renderInlineFallback).join("<br>")}</p>`);
    paragraph = [];
  };
  const flushList = () => {
    if (!list.length) {
      return;
    }
    html.push(`<ul>${list.map((item) => `<li>${renderInlineFallback(item)}</li>`).join("")}</ul>`);
    list = [];
  };
  const flushQuote = () => {
    if (!quote.length) {
      return;
    }
    html.push(`<blockquote>${quote.map(renderInlineFallback).join("<br>")}</blockquote>`);
    quote = [];
  };
  const flushOpenBlocks = () => {
    flushParagraph();
    flushList();
    flushQuote();
  };

  lines.forEach((line) => {
    if (/^```/.test(line)) {
      if (inCode) {
        html.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
        code = [];
        inCode = false;
      } else {
        flushOpenBlocks();
        inCode = true;
      }
      return;
    }
    if (inCode) {
      code.push(line);
      return;
    }

    if (!line.trim()) {
      flushOpenBlocks();
      return;
    }

    const heading = line.match(/^(#{1,6})\s+(.+)$/);
    if (heading) {
      flushOpenBlocks();
      const level = heading[1].length;
      html.push(`<h${level}>${renderInlineFallback(heading[2])}</h${level}>`);
      return;
    }

    const listItem = line.match(/^\s*[-*]\s+(.+)$/);
    if (listItem) {
      flushParagraph();
      flushQuote();
      list.push(listItem[1]);
      return;
    }

    const quoted = line.match(/^>\s?(.*)$/);
    if (quoted) {
      flushParagraph();
      flushList();
      quote.push(quoted[1]);
      return;
    }

    flushList();
    flushQuote();
    paragraph.push(line);
  });

  if (inCode) {
    html.push(`<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`);
  }
  flushOpenBlocks();
  return html.join("\n");
}

function markdownHref(path, hash = "") {
  if (!path) {
    return hash ? `#${encodeURIComponent(hash)}` : "#";
  }
  const encoded = encodePath(path);
  return hash ? `${encoded}#${encodeURIComponent(hash)}` : encoded;
}

function parseWikiRef(raw = "") {
  const [targetWithHash, labelFromPipe] = raw.split("|");
  const hashIndex = targetWithHash.indexOf("#");
  const target = hashIndex >= 0 ? targetWithHash.slice(0, hashIndex).trim() : targetWithHash.trim();
  const hash = hashIndex >= 0 ? targetWithHash.slice(hashIndex + 1).trim() : "";
  const label = (labelFromPipe || hash || target || raw).trim();
  return { target, hash, label };
}

function preprocessObsidianLinks(markdown, basePath) {
  const parts = markdown.split(/(```[\s\S]*?```|`[^`\n]+`)/g);
  return parts
    .map((part) => {
      if (!part || part.startsWith("```") || part.startsWith("`")) {
        return part;
      }
      return part
        .replace(/!\[\[([^\]]+)\]\]/g, (_, raw) => {
          const ref = parseWikiRef(raw);
          const targetPath = findFileByReference(ref.target, basePath);
          if (!targetPath) {
            return `[[${raw}]]`;
          }
          const label = escapeMarkdownLabel(ref.label || basename(targetPath));
          if (GROUPS.images.extensions.has(extOf(targetPath))) {
            return `![${label}](${markdownHref(targetPath, ref.hash)})`;
          }
          return `[${label}](${markdownHref(targetPath, ref.hash)})`;
        })
        .replace(/\[\[([^\]]+)\]\]/g, (_, raw) => {
          const ref = parseWikiRef(raw);
          const targetPath = ref.target ? findFileByReference(ref.target, basePath) : basePath;
          if (!targetPath && ref.target) {
            return `[[${raw}]]`;
          }
          const label = escapeMarkdownLabel(ref.label || ref.hash || basename(targetPath));
          return `[${label}](${markdownHref(targetPath, ref.hash)})`;
        });
    })
    .join("");
}

function preprocessLocalFileLinks(markdown) {
  const parts = markdown.split(/(```[\s\S]*?```|`[^`\n]+`)/g);
  return parts
    .map((part) => {
      if (!part || part.startsWith("```") || part.startsWith("`")) {
        return part;
      }
      return part
        .replace(/\[([^\]]+)\]\(<file:[^)]+>\)/gi, (_, label) => `<span class="local-file-link">${escapeHtml(label)}</span>`)
        .replace(/\[([^\]]+)\]\(file:[^)]+\)/gi, (_, label) => `<span class="local-file-link">${escapeHtml(label)}</span>`);
    })
    .join("");
}

function normalizeMathDelimiters(markdown) {
  const parts = markdown.split(/(```[\s\S]*?```|`[^`\n]+`)/g);
  return parts
    .map((part) => {
      if (!part || part.startsWith("```") || part.startsWith("`")) {
        return part;
      }
      return part
        .replace(/\\\[([\s\S]*?)\\\]/g, (_, expr) => `\n$$\n${expr.trim()}\n$$\n`)
        .replace(/\\\(([\s\S]*?)\\\)/g, (_, expr) => `$${expr.trim()}$`);
    })
    .join("");
}

function stripFrontMatter(markdown) {
  const match = markdown.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n+/);
  if (!match || !/(^|\n)[A-Za-z0-9_-]+:\s*/.test(match[1])) {
    return markdown;
  }
  return markdown.slice(match[0].length);
}

function stripLeadingTitle(markdown, title) {
  const match = markdown.match(/^#\s+(.+?)\r?\n+/);
  if (!match || normalize(match[1]) !== normalize(title)) {
    return markdown;
  }
  return markdown.slice(match[0].length).replace(/^\s+/, "");
}

function slugifyHeading(text, index) {
  const slug = text
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9\u4e00-\u9fff]+/g, "-")
    .replace(/^-+|-+$/g, "");
  return slug || `section-${index + 1}`;
}

function scrollToAnchor(anchor) {
  if (!anchor) {
    return;
  }
  const target = document.getElementById(anchor) || document.getElementById(slugifyHeading(anchor, 0));
  if (target) {
    target.scrollIntoView({ block: "start" });
  }
}

function renderStats() {
  elements.libraryStats.textContent = [
    `${state.files.length} 个文件`,
    `笔记 ${state.counts.notes || 0}`,
    `图片 ${state.counts.images || 0}`,
    `数据 ${state.counts.data || 0}`,
    `文档 ${state.counts.files || 0}`
  ].join(" · ");
}

function renderTypeFilters() {
  elements.typeFilters.innerHTML = "";
  Object.entries(GROUPS).forEach(([key, group]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `filter-chip${state.group === key ? " is-active" : ""}`;
    button.textContent = `${group.label} ${state.counts[key] || 0}`;
    button.setAttribute("aria-pressed", state.group === key ? "true" : "false");
    button.addEventListener("click", () => {
      state.group = key;
      state.visibleLimit = LIST_PAGE_SIZE;
      renderTypeFilters();
      renderFileList();
    });
    elements.typeFilters.appendChild(button);
  });
}

function renderQuickLinks() {
  elements.quickLinks.innerHTML = "";
  QUICK_LINKS.forEach(([label, path]) => {
    if (!state.byPath.has(path)) {
      return;
    }
    const button = document.createElement("button");
    button.type = "button";
    button.className = "quick-link";
    button.textContent = label;
    button.addEventListener("click", () => setRoute(path));
    elements.quickLinks.appendChild(button);
  });
}

function fileMatches(file, query) {
  if (state.group !== "all" && groupForExt(file.ext) !== state.group) {
    return false;
  }
  if (!query) {
    return true;
  }
  return normalize([file.title, file.name, file.path, file.category, file.ext].join(" ")).includes(query);
}

function scoreFile(file, query) {
  if (!query) {
    return 0;
  }

  const title = normalize(file.title);
  const name = normalize(file.name);
  const path = normalize(file.path);
  const category = normalize(file.category);
  const ext = normalize(file.ext);
  const terms = query.split(/\s+/).filter(Boolean);

  return terms.reduce((score, term) => {
    if (title === term) score += 120;
    else if (title.startsWith(term)) score += 95;
    else if (title.includes(term)) score += 75;

    if (name === term) score += 100;
    else if (name.startsWith(term)) score += 80;
    else if (name.includes(term)) score += 60;

    if (path.includes(term)) score += 42;
    if (category.includes(term)) score += 24;
    if (ext === term) score += 10;

    return score;
  }, 0) - Math.min(file.path.length / 500, 8);
}

function createFileButton(file, options = {}) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = [
    "file-item",
    file.path === state.activePath ? "is-active" : "",
    options.pinned ? "is-pinned" : ""
  ].filter(Boolean).join(" ");

  const badge = document.createElement("span");
  badge.className = "file-badge";
  badge.textContent = file.ext ? file.ext.toUpperCase() : "FILE";

  const text = document.createElement("span");
  text.className = "file-text";

  if (options.pinned) {
    const current = document.createElement("span");
    current.className = "file-current-label";
    current.textContent = "当前打开";
    text.appendChild(current);
  }

  const title = document.createElement("span");
  title.className = "file-title";
  title.textContent = file.title || file.name;

  const path = document.createElement("span");
  path.className = "file-path";
  path.textContent = file.path;

  text.append(title, path);
  button.append(badge, text);
  button.addEventListener("click", () => setRoute(file.path));
  return button;
}

function renderFileList() {
  const query = normalize(state.query);
  const allMatches = state.files.filter((file) => fileMatches(file, query));
  if (query) {
    allMatches.sort((a, b) => scoreFile(b, query) - scoreFile(a, query) || a.path.localeCompare(b.path, "zh-Hans-CN"));
  }
  const matches = allMatches.slice(0, state.visibleLimit);

  elements.resultCount.textContent = query
    ? `${allMatches.length} 个匹配，显示 ${matches.length} 个`
    : `${allMatches.length} 个文件，显示 ${matches.length} 个`;

  elements.fileList.innerHTML = "";
  const fragment = document.createDocumentFragment();
  const activeFile = state.activePath ? state.byPath.get(state.activePath) : null;
  const activeVisible = activeFile && matches.some((file) => file.path === activeFile.path);
  if (activeFile && !activeVisible) {
    fragment.appendChild(createFileButton(activeFile, { pinned: true }));
  }

  if (!allMatches.length) {
    const empty = document.createElement("div");
    empty.className = "empty-list";
    empty.textContent = "没有找到匹配文件。";
    fragment.appendChild(empty);
    elements.fileList.appendChild(fragment);
    return;
  }

  matches.forEach((file) => {
    fragment.appendChild(createFileButton(file));
  });

  if (allMatches.length > matches.length) {
    const more = document.createElement("button");
    more.type = "button";
    more.className = "more-button";
    more.textContent = `继续显示 ${Math.min(LIST_PAGE_SIZE, allMatches.length - matches.length)} 个`;
    more.addEventListener("click", () => {
      state.visibleLimit += LIST_PAGE_SIZE;
      renderFileList();
    });
    fragment.appendChild(more);
  }

  elements.fileList.appendChild(fragment);
}

function renderToc() {
  const headings = Array.from(elements.content.querySelectorAll("h2, h3, h4"));
  elements.toc.innerHTML = "";
  if (!headings.length) {
    elements.toc.classList.add("is-hidden");
    return;
  }

  const title = document.createElement("div");
  title.className = "toc-title";
  title.textContent = "本页目录";

  const list = document.createElement("div");
  list.className = "toc-list";

  const seen = new Map();
  headings.forEach((heading, index) => {
    const text = heading.textContent.replace(/\s+/g, " ").trim();
    const base = slugifyHeading(text, index);
    const count = (seen.get(base) || 0) + 1;
    seen.set(base, count);
    const id = count === 1 ? base : `${base}-${count}`;
    heading.id = id;

    const link = document.createElement("a");
    link.className = `level-${heading.tagName.slice(1)}`;
    link.href = "#";
    link.textContent = text;
    link.addEventListener("click", (event) => {
      event.preventDefault();
      heading.scrollIntoView({ block: "start" });
    });
    list.appendChild(link);
  });

  elements.toc.append(title, list);
  elements.toc.classList.remove("is-hidden");
}

function rewriteRenderedLinks(basePath) {
  elements.content.querySelectorAll("img[src]").forEach((img) => {
    const source = img.getAttribute("src");
    const resolved = resolveRelative(basePath, source);
    if (!resolved.external && resolved.path && state.byPath.has(resolved.path)) {
      img.src = fileUrl(resolved.path);
      img.loading = "lazy";
    }
  });

  elements.content.querySelectorAll("a[href]").forEach((link) => {
    const href = link.getAttribute("href");
    if (!href) {
      return;
    }
    if (href.startsWith("#")) {
      const anchor = safeDecode(href.slice(1));
      link.addEventListener("click", (event) => {
        event.preventDefault();
        scrollToAnchor(anchor);
      });
      return;
    }
    if (/^file:/i.test(href)) {
      link.href = "#";
      link.classList.add("local-file-link");
      link.title = "这个本地文件没有直接发布到网页。";
      link.addEventListener("click", (event) => event.preventDefault());
      return;
    }
    if (/^[a-z]+:/i.test(href)) {
      link.target = "_blank";
      link.rel = "noopener";
      return;
    }

    const resolved = resolveRelative(basePath, href);
    if (!resolved.path || resolved.external || !state.byPath.has(resolved.path)) {
      return;
    }

    const ext = extOf(resolved.path);
    if (["md", "txt", "json", "csv", "py", "ps1", "html", "htm", "url", ""].includes(ext)) {
      link.href = "#";
      link.addEventListener("click", (event) => {
        event.preventDefault();
        setRoute(resolved.path, resolved.hash);
      });
    } else {
      link.href = fileUrl(resolved.path);
      link.target = "_blank";
      link.rel = "noopener";
    }
  });
}

async function fetchUtf8Text(path, limit = TEXT_PREVIEW_LIMIT) {
  const response = await fetch(fileUrl(path), { cache: "no-cache" });
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  const buffer = await response.arrayBuffer();
  const tooLarge = buffer.byteLength > limit;
  const slice = tooLarge ? buffer.slice(0, limit) : buffer;
  return {
    text: new TextDecoder("utf-8").decode(slice),
    bytes: buffer.byteLength,
    tooLarge
  };
}

async function renderMarkdown(file, text, anchor = "") {
  const cleaned = stripLeadingTitle(stripFrontMatter(text), file.title);
  const source = normalizeMathDelimiters(preprocessLocalFileLinks(preprocessObsidianLinks(cleaned, file.path)));
  const rendered = window.marked ? marked.parse(source) : basicMarkdownToHtml(source);

  if (window.MathJax?.typesetClear) {
    window.MathJax.typesetClear([elements.content]);
  }

  elements.content.innerHTML = window.DOMPurify
    ? DOMPurify.sanitize(rendered, { USE_PROFILES: { html: true } })
    : rendered;

  rewriteRenderedLinks(file.path);
  renderToc();

  if (window.MathJax?.typesetPromise) {
    await window.MathJax.typesetPromise([elements.content]);
  }
  scrollToAnchor(anchor);
}

function renderText(text, language = "", options = {}) {
  elements.toc.classList.add("is-hidden");
  elements.toc.innerHTML = "";
  const notice = options.tooLarge
    ? `<div class="preview-note">文件较大，当前只预览前 ${displaySize(TEXT_PREVIEW_LIMIT)}；完整内容请打开原文件。</div>`
    : "";
  elements.content.innerHTML = `${notice}<pre><code class="language-${escapeHtml(language)}">${escapeHtml(text)}</code></pre>`;
}

function renderImage(file) {
  elements.toc.classList.add("is-hidden");
  elements.toc.innerHTML = "";
  const url = fileUrl(file.path);
  elements.content.innerHTML = `
    <figure class="image-preview">
      <a href="${url}" target="_blank" rel="noopener">
        <img src="${url}" alt="${escapeHtml(file.title || file.name)}" loading="lazy">
      </a>
      <figcaption>${escapeHtml(file.path)} · ${displaySize(file.size)}</figcaption>
    </figure>
  `;
}

function renderHtml(file) {
  elements.toc.classList.add("is-hidden");
  elements.toc.innerHTML = "";
  elements.content.innerHTML = `<iframe class="html-frame" title="${escapeHtml(file.title)}" src="${fileUrl(file.path)}"></iframe>`;
}

function renderDownloadCard(file) {
  elements.toc.classList.add("is-hidden");
  elements.toc.innerHTML = "";
  const url = fileUrl(file.path);
  elements.content.innerHTML = `
    <section class="asset-card">
      <p class="asset-kicker">${escapeHtml(file.ext ? file.ext.toUpperCase() : "文件")} · ${displaySize(file.size)}</p>
      <h3>${escapeHtml(file.title || file.name)}</h3>
      <p class="asset-path">${escapeHtml(file.path)}</p>
      <div class="asset-actions">
        <a class="button" href="${url}" target="_blank" rel="noopener">打开原文件</a>
        <a class="button button-secondary" href="${url}" download>下载</a>
      </div>
    </section>
  `;
}

async function openFile(path, anchor = "") {
  const requestId = ++state.openRequestId;
  const file = state.byPath.get(path);
  if (!file) {
    elements.fileTitle.textContent = "没有找到文件";
    elements.fileMeta.textContent = "";
    elements.rawLink.href = "#";
    elements.content.innerHTML = '<div class="empty-state">这个文件不在当前发布清单里。</div>';
    return;
  }

  state.activePath = path;
  document.title = file.title === "高中数学复习系统" ? file.title : `${file.title} | 高中数学复习系统`;
  elements.fileTitle.textContent = file.title;
  elements.fileMeta.textContent = `${file.category || file.ext.toUpperCase() || "文件"} · ${displaySize(file.size)} · ${file.path}`;
  elements.rawLink.href = fileUrl(file.path);
  renderFileList();

  const ext = extOf(path);
  try {
    if (GROUPS.images.extensions.has(ext)) {
      renderImage(file);
      return;
    }
    if (ext === "html" || ext === "htm") {
      renderHtml(file);
      return;
    }
    if (GROUPS.files.extensions.has(ext)) {
      renderDownloadCard(file);
      return;
    }

    const { text, tooLarge } = await fetchUtf8Text(path);
    if (requestId !== state.openRequestId || state.activePath !== path) {
      return;
    }
    if (ext === "md") {
      await renderMarkdown(file, text, anchor);
    } else if (ext === "json" && !tooLarge) {
      renderText(JSON.stringify(JSON.parse(text), null, 2), "json");
    } else {
      renderText(text, ext || "text", { tooLarge });
    }
  } catch (error) {
    console.error(error);
    elements.content.innerHTML = '<div class="empty-state">文件读取失败，可能是浏览器缓存或发布尚未完成。</div>';
  }
}

async function loadManifest() {
  const response = await fetch("./manifest.json", { cache: "no-cache" });
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  const text = new TextDecoder("utf-8").decode(await response.arrayBuffer());
  return JSON.parse(text);
}

async function init() {
  elements.search.addEventListener("input", (event) => {
    state.query = event.target.value;
    state.visibleLimit = LIST_PAGE_SIZE;
    renderFileList();
  });

  window.addEventListener("hashchange", () => {
    openFile(pathFromRoute() || "README.md", anchorFromRoute());
  });

  const manifest = await loadManifest();
  state.files = manifest.files.map((file) => ({
    ...file,
    ext: extOf(file.path),
    name: basename(file.path)
  }));
  state.byPath = new Map(state.files.map((file) => [file.path, file]));
  buildIndexes();

  renderStats();
  renderTypeFilters();
  renderQuickLinks();
  renderFileList();
  openFile(pathFromRoute() || "README.md", anchorFromRoute());
}

init().catch((error) => {
  console.error(error);
  elements.libraryStats.textContent = "资料库载入失败";
  elements.fileTitle.textContent = "载入失败";
  elements.content.innerHTML = '<div class="empty-state">清单载入失败，请稍后刷新。</div>';
});
