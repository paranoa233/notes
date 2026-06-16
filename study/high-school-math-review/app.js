const state = {
  files: [],
  byPath: new Map(),
  activePath: "",
  query: ""
};

const quickLinks = [
  ["学习工作台", "学习工作台.md"],
  ["互动工作台", "学习工作台.html"],
  ["LLM Wiki", "LLM知识库/wiki/00_Index.md"],
  ["二轮题库", "Obsidian题库/README.md"],
  ["五年经典", "高考数学五年经典/README.md"],
  ["个人错题库", "个人错题库/README.md"],
  ["AI 笔记", "Obsidian题库/08_AI笔记管理/AI学习流水线.md"],
  ["大文件清单", "未上传大文件清单.md"]
];

const elements = {
  search: document.getElementById("search"),
  quickLinks: document.getElementById("quick-links"),
  fileList: document.getElementById("file-list"),
  resultCount: document.getElementById("result-count"),
  fileTitle: document.getElementById("file-title"),
  fileMeta: document.getElementById("file-meta"),
  rawLink: document.getElementById("raw-link"),
  content: document.getElementById("content"),
  toc: document.getElementById("toc")
};

marked.setOptions({
  breaks: true,
  gfm: true
});

function normalize(text = "") {
  return text.toLowerCase().trim();
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

function displaySize(bytes) {
  if (bytes < 1024) {
    return `${bytes} B`;
  }
  if (bytes < 1024 * 1024) {
    return `${(bytes / 1024).toFixed(1)} KB`;
  }
  return `${(bytes / 1024 / 1024).toFixed(2)} MB`;
}

function extOf(path) {
  const match = path.match(/\.([^.\/]+)$/);
  return match ? match[1].toLowerCase() : "";
}

function dirname(path) {
  const index = path.lastIndexOf("/");
  return index >= 0 ? path.slice(0, index) : "";
}

function normalizePath(path) {
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

function resolveRelative(basePath, href) {
  const [withoutHash] = href.split("#");
  const [cleanPath] = withoutHash.split("?");
  if (!cleanPath || /^[a-z]+:/i.test(cleanPath) || cleanPath.startsWith("/")) {
    return cleanPath;
  }
  const baseDir = dirname(basePath);
  return normalizePath(`${baseDir}/${decodeURIComponent(cleanPath)}`);
}

function setRoute(path) {
  const hash = `#file=${encodeURIComponent(path)}`;
  if (window.location.hash !== hash) {
    window.location.hash = hash;
  } else {
    openFile(path);
  }
}

function pathFromRoute() {
  const params = new URLSearchParams(window.location.hash.slice(1));
  return params.get("file");
}

function renderQuickLinks() {
  elements.quickLinks.innerHTML = "";
  quickLinks.forEach(([label, path]) => {
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
  if (!query) {
    return true;
  }
  return normalize([file.title, file.path, file.category, file.ext].join(" ")).includes(query);
}

function renderFileList() {
  const query = normalize(state.query);
  const matches = state.files.filter((file) => fileMatches(file, query)).slice(0, 180);
  const total = state.files.filter((file) => fileMatches(file, query)).length;

  elements.resultCount.textContent = query
    ? `${total} 个匹配，显示前 ${matches.length} 个`
    : `${state.files.length} 个轻量文件`;

  elements.fileList.innerHTML = "";
  matches.forEach((file) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `file-item${file.path === state.activePath ? " is-active" : ""}`;

    const title = document.createElement("span");
    title.className = "file-title";
    title.textContent = file.title || file.name;

    const path = document.createElement("span");
    path.className = "file-path";
    path.textContent = file.path;

    button.append(title, path);
    button.addEventListener("click", () => setRoute(file.path));
    elements.fileList.appendChild(button);
  });
}

function stripLeadingTitle(markdown, title) {
  const match = markdown.match(/^#\s+(.+?)\r?\n+/);
  if (!match) {
    return markdown;
  }
  if (normalize(match[1]) !== normalize(title)) {
    return markdown;
  }
  return markdown.slice(match[0].length).replace(/^\s+/, "");
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

function slugifyHeading(text, index) {
  const slug = text
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9\u4e00-\u9fff]+/g, "-")
    .replace(/^-+|-+$/g, "");
  return slug || `section-${index + 1}`;
}

function renderToc() {
  const headings = Array.from(elements.content.querySelectorAll("h2, h3, h4"));
  if (!headings.length) {
    elements.toc.classList.add("is-hidden");
    elements.toc.innerHTML = "";
    return;
  }

  const seen = new Map();
  const items = headings.map((heading, index) => {
    const text = heading.textContent.replace(/\s+/g, " ").trim();
    const base = slugifyHeading(text, index);
    const count = (seen.get(base) || 0) + 1;
    seen.set(base, count);
    const id = count === 1 ? base : `${base}-${count}`;
    heading.id = id;
    return { id, text, level: Number(heading.tagName.slice(1)) };
  });

  const list = items
    .map((item) => `<a class="level-${item.level}" href="#${item.id}">${item.text}</a>`)
    .join("");
  elements.toc.innerHTML = `<div class="toc-title">本页目录</div><div class="toc-list">${list}</div>`;
  elements.toc.classList.remove("is-hidden");
}

function rewriteRenderedLinks(basePath) {
  elements.content.querySelectorAll("img[src]").forEach((img) => {
    const source = img.getAttribute("src");
    const resolved = resolveRelative(basePath, source);
    if (resolved && state.byPath.has(resolved)) {
      img.src = fileUrl(resolved);
    }
  });

  elements.content.querySelectorAll("a[href]").forEach((link) => {
    const href = link.getAttribute("href");
    if (!href || href.startsWith("#") || /^[a-z]+:/i.test(href)) {
      return;
    }
    const resolved = resolveRelative(basePath, href);
    if (!resolved || !state.byPath.has(resolved)) {
      return;
    }
    const ext = extOf(resolved);
    if (["md", "txt", "json", "csv", "py", "ps1", "html", "htm"].includes(ext)) {
      link.href = `#file=${encodeURIComponent(resolved)}`;
      link.addEventListener("click", (event) => {
        event.preventDefault();
        setRoute(resolved);
      });
    } else {
      link.href = fileUrl(resolved);
      link.target = "_blank";
      link.rel = "noopener";
    }
  });
}

async function renderMarkdown(file, text) {
  const markdown = normalizeMathDelimiters(stripLeadingTitle(text, file.title));
  const rendered = marked.parse(markdown);

  if (window.MathJax?.typesetClear) {
    window.MathJax.typesetClear([elements.content]);
  }

  elements.content.innerHTML = DOMPurify.sanitize(rendered, {
    USE_PROFILES: { html: true }
  });
  rewriteRenderedLinks(file.path);
  renderToc();

  if (window.MathJax?.typesetPromise) {
    await window.MathJax.typesetPromise([elements.content]);
  }
}

function renderText(text, language = "") {
  elements.toc.classList.add("is-hidden");
  elements.toc.innerHTML = "";
  const escaped = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
  elements.content.innerHTML = `<pre><code class="language-${language}">${escaped}</code></pre>`;
}

function renderHtml(file) {
  elements.toc.classList.add("is-hidden");
  elements.toc.innerHTML = "";
  elements.content.innerHTML = `<iframe class="html-frame" title="${file.title}" src="${fileUrl(file.path)}"></iframe>`;
}

async function openFile(path) {
  const file = state.byPath.get(path);
  if (!file) {
    elements.fileTitle.textContent = "没有找到文件";
    elements.fileMeta.textContent = "";
    elements.rawLink.href = "#";
    elements.content.innerHTML = '<div class="empty-state">这个文件不在当前发布清单里。</div>';
    return;
  }

  state.activePath = path;
  document.title = `${file.title} | 高中数学复习系统`;
  elements.fileTitle.textContent = file.title;
  elements.fileMeta.textContent = `${file.category || file.ext.toUpperCase()} · ${displaySize(file.size)} · ${file.path}`;
  elements.rawLink.href = fileUrl(file.path);
  renderFileList();

  const ext = extOf(path);
  try {
    if (ext === "html" || ext === "htm") {
      renderHtml(file);
      return;
    }

    const response = await fetch(fileUrl(path));
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const text = await response.text();

    if (ext === "md") {
      await renderMarkdown(file, text);
    } else if (ext === "json") {
      renderText(JSON.stringify(JSON.parse(text), null, 2), "json");
    } else {
      renderText(text, ext);
    }
  } catch (error) {
    console.error(error);
    elements.content.innerHTML = '<div class="empty-state">文件读取失败，可能是浏览器缓存或发布尚未完成。</div>';
  }
}

async function init() {
  elements.search.addEventListener("input", (event) => {
    state.query = event.target.value;
    renderFileList();
  });

  window.addEventListener("hashchange", () => {
    openFile(pathFromRoute() || "README.md");
  });

  const response = await fetch("./manifest.json");
  const manifest = await response.json();
  state.files = manifest.files;
  state.byPath = new Map(state.files.map((file) => [file.path, file]));

  renderQuickLinks();
  renderFileList();
  openFile(pathFromRoute() || "README.md");
}

init().catch((error) => {
  console.error(error);
  elements.fileTitle.textContent = "载入失败";
  elements.content.innerHTML = '<div class="empty-state">清单载入失败，请稍后刷新。</div>';
});
