const SITE_TITLE = "paranoa233's notes";
const DEFAULT_DESCRIPTION =
  "paranoa233 的独立文章阅读页，采用白纸黑字的阅读模式。";
const BUILD_ID = "20260413-4";

const elements = {
  articleDate: document.getElementById("article-date"),
  articleTitle: document.getElementById("article-title"),
  articleTags: document.getElementById("article-tags"),
  articleToc: document.getElementById("article-toc"),
  article: document.getElementById("article"),
  articleNav: document.getElementById("article-nav"),
  metaDescription: document.querySelector('meta[name="description"]')
};

marked.setOptions({
  breaks: false,
  gfm: true
});

function normalize(text = "") {
  return text.toLowerCase().trim();
}

function getSlugFromQuery() {
  const params = new URLSearchParams(window.location.search);
  return params.get("slug");
}

function setPageMeta(note) {
  document.title = note ? `${note.title} | ${SITE_TITLE}` : SITE_TITLE;

  if (elements.metaDescription) {
    elements.metaDescription.content = note?.summary || DEFAULT_DESCRIPTION;
  }
}

function renderTags(note) {
  elements.articleTags.innerHTML = "";

  note.tags.forEach((tag) => {
    const span = document.createElement("span");
    span.className = "article-tag";
    span.textContent = tag;
    elements.articleTags.appendChild(span);
  });
}

function getNavGroup(note) {
  return note.navGroup || "default";
}

function renderArticleNav(notes, currentNote) {
  elements.articleNav.innerHTML = "";

  const sequence = notes.filter(
    (note) => !note.excludeFromNav && getNavGroup(note) === getNavGroup(currentNote)
  );
  const currentIndex = sequence.findIndex((note) => note.slug === currentNote.slug);

  const previous = sequence[currentIndex - 1];
  const next = sequence[currentIndex + 1];

  if (previous) {
    const prevLink = document.createElement("a");
    prevLink.className = "nav-link";
    prevLink.href = `./note.html?slug=${encodeURIComponent(previous.slug)}`;

    const prevLabel = document.createElement("span");
    prevLabel.textContent = "上一篇";

    const prevTitle = document.createElement("strong");
    prevTitle.textContent = previous.title;

    prevLink.append(prevLabel, prevTitle);
    elements.articleNav.appendChild(prevLink);
  }

  if (next) {
    const nextLink = document.createElement("a");
    nextLink.className = "nav-link";
    nextLink.href = `./note.html?slug=${encodeURIComponent(next.slug)}`;

    const nextLabel = document.createElement("span");
    nextLabel.textContent = "下一篇";

    const nextTitle = document.createElement("strong");
    nextTitle.textContent = next.title;

    nextLink.append(nextLabel, nextTitle);
    elements.articleNav.appendChild(nextLink);
  }
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

function escapeHtml(text) {
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function protectMathSegments(markdown) {
  const parts = markdown.split(/(```[\s\S]*?```|`[^`\n]+`)/g);
  const segments = [];
  let counter = 0;

  function createToken(content) {
    const token = `CODEXMATH${counter}TOKEN`;
    counter += 1;
    segments.push({ token, content });
    return token;
  }

  const protectedMarkdown = parts
    .map((part) => {
      if (!part || part.startsWith("```") || part.startsWith("`")) {
        return part;
      }

      return part
        .replace(/\\\[[\s\S]*?\\\]/g, (match) => createToken(match))
        .replace(/\\\([\s\S]*?\\\)/g, (match) => createToken(match))
        .replace(/(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$/g, (match) => createToken(match))
        .replace(/(?<!\\)\$(?!\$)(?:\\.|[^$\n])+?(?<!\\)\$(?!\$)/g, (match) =>
          createToken(match)
        );
    })
    .join("");

  return { protectedMarkdown, segments };
}

function restoreMathSegments(html, segments) {
  return segments.reduce((current, segment) => {
    return current.replaceAll(segment.token, escapeHtml(segment.content));
  }, html);
}

function formatLanguageLabel(language) {
  const labelMap = {
    js: "JavaScript",
    jsx: "React JSX",
    ts: "TypeScript",
    tsx: "React TSX",
    py: "Python",
    sh: "Shell",
    bash: "Bash",
    ps1: "PowerShell",
    yml: "YAML",
    md: "Markdown",
    html: "HTML",
    css: "CSS",
    json: "JSON",
    cpp: "C++",
    csharp: "C#",
    plaintext: "Text",
    text: "Text"
  };

  if (!language) {
    return "Text";
  }

  const normalized = language.toLowerCase();
  return labelMap[normalized] || normalized.toUpperCase();
}

function getCodeLanguage(block) {
  const match = block.className.match(/language-([a-z0-9#+_-]+)/i);
  return match?.[1] || "";
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

function buildTableOfContents() {
  const headings = Array.from(elements.article.querySelectorAll("h2, h3, h4"));
  const seen = new Map();

  return headings
    .map((heading, index) => {
      const text = heading.textContent.replace(/\s+/g, " ").trim();
      if (!text) {
        return null;
      }

      const baseId = slugifyHeading(text, index);
      const currentCount = seen.get(baseId) || 0;
      const nextCount = currentCount + 1;
      seen.set(baseId, nextCount);

      const id = nextCount === 1 ? baseId : `${baseId}-${nextCount}`;
      heading.id = id;

      return {
        id,
        text,
        level: Number(heading.tagName.slice(1))
      };
    })
    .filter(Boolean);
}

function renderTableOfContents(items) {
  if (!items.length) {
    elements.articleToc.innerHTML = "";
    elements.articleToc.classList.add("is-hidden");
    return;
  }

  elements.articleToc.classList.remove("is-hidden");
  elements.articleToc.innerHTML = "";

  const title = document.createElement("div");
  title.className = "article-toc-title";
  title.textContent = "本页目录";

  const list = document.createElement("div");
  list.className = "article-toc-list";

  items.forEach((item) => {
    const link = document.createElement("a");
    link.className = `article-toc-link level-${item.level}`;
    link.href = `#${item.id}`;
    link.textContent = item.text;
    list.appendChild(link);
  });

  elements.articleToc.append(title, list);
}

function decorateHeadings(items) {
  items.forEach((item) => {
    const heading = document.getElementById(item.id);
    if (!heading || heading.querySelector(".heading-anchor")) {
      return;
    }

    const anchor = document.createElement("a");
    anchor.className = "heading-anchor";
    anchor.href = `#${item.id}`;
    anchor.textContent = "#";
    anchor.setAttribute("aria-label", `链接到 ${item.text}`);
    heading.appendChild(anchor);
  });
}

function markLeadParagraph() {
  const lead = Array.from(elements.article.children).find((node) => {
    return node.tagName === "P" && node.textContent.trim();
  });

  if (lead) {
    lead.classList.add("article-lead");
  }
}

function wrapTables() {
  elements.article.querySelectorAll("table").forEach((table) => {
    if (table.parentElement?.classList.contains("table-scroll")) {
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.className = "table-scroll";
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  });
}

function enhanceFigures() {
  elements.article.querySelectorAll("p > img:only-child").forEach((image) => {
    const paragraph = image.parentElement;
    const figure = document.createElement("figure");
    figure.className = "article-figure";

    paragraph.parentNode.insertBefore(figure, paragraph);
    figure.appendChild(image);

    const alt = image.getAttribute("alt")?.trim();
    if (alt) {
      const caption = document.createElement("figcaption");
      caption.textContent = alt;
      figure.appendChild(caption);
    }

    paragraph.remove();
  });

  elements.article.querySelectorAll("img").forEach((image) => {
    image.loading = "lazy";
    image.decoding = "async";
  });
}

function enhanceCodeBlocks() {
  elements.article.querySelectorAll("pre > code").forEach((block) => {
    const pre = block.parentElement;
    let language = getCodeLanguage(block);

    if (window.hljs) {
      if (language && window.hljs.getLanguage(language)) {
        window.hljs.highlightElement(block);
      } else {
        const result = window.hljs.highlightAuto(block.textContent);
        block.innerHTML = result.value;
        block.classList.add("hljs");
        language = result.language || language;
      }
    }

    pre.classList.add("code-block");
    pre.dataset.language = formatLanguageLabel(language);
  });
}

function enhanceLinks() {
  elements.article.querySelectorAll("a[href]").forEach((link) => {
    const href = link.getAttribute("href");
    if (!href || href.startsWith("#")) {
      return;
    }

    if (/^https?:\/\//i.test(href)) {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    }
  });
}

function decorateTaskLists() {
  elements.article.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
    checkbox.disabled = true;
  });
}

function decorateRenderedContent() {
  wrapTables();
  enhanceFigures();
  enhanceCodeBlocks();
  enhanceLinks();
  decorateTaskLists();
  markLeadParagraph();
}

function showError(title, message) {
  setPageMeta();
  elements.articleTitle.textContent = title;
  elements.articleDate.textContent = "";
  elements.articleTags.innerHTML = "";
  elements.articleToc.innerHTML = "";
  elements.articleToc.classList.add("is-hidden");
  elements.articleNav.innerHTML = "";
  elements.article.innerHTML = `<div class="empty-state">${message}</div>`;
}

async function openNote(note, notes) {
  elements.articleTitle.textContent = note.title;
  elements.articleDate.textContent = note.date || "";
  renderTags(note);
  setPageMeta(note);
  renderArticleNav(notes, note);

  try {
    const response = await fetch(`./notes/${note.file}?v=${BUILD_ID}`, {
      cache: "no-store"
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const markdown = await response.text();
    const cleanedMarkdown = stripLeadingTitle(markdown, note.title);
    const { protectedMarkdown, segments } = protectMathSegments(cleanedMarkdown);
    const rendered = restoreMathSegments(marked.parse(protectedMarkdown), segments);

    if (window.MathJax?.typesetClear) {
      window.MathJax.typesetClear([elements.article]);
    }

    elements.article.innerHTML = DOMPurify.sanitize(rendered, {
      USE_PROFILES: { html: true }
    });
    const tocItems = buildTableOfContents();
    decorateRenderedContent();
    decorateHeadings(tocItems);
    renderTableOfContents(tocItems);

    if (window.MathJax?.typesetPromise) {
      await window.MathJax.typesetPromise([elements.article]);
    }
  } catch (error) {
    console.error(error);
    elements.articleToc.innerHTML = "";
    elements.articleToc.classList.add("is-hidden");
    elements.article.innerHTML =
      '<div class="empty-state">文章读取失败。请确认对应的 Markdown 文件已经存在并成功推送。</div>';
  }
}

async function init() {
  try {
    const response = await fetch(`./notes/notes.json?v=${BUILD_ID}`, {
      cache: "no-store"
    });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const notes = await response.json();
    if (!notes.length) {
      showError("还没有文章", "当前还没有可阅读的文章。");
      return;
    }

    const slug = getSlugFromQuery() || notes[0].slug;
    const currentIndex = notes.findIndex((note) => note.slug === slug);

    if (currentIndex < 0) {
      showError("未找到文章", "没有找到对应文章，请返回主页重新打开。");
      return;
    }

    if (!getSlugFromQuery()) {
      const nextUrl = `./note.html?slug=${encodeURIComponent(slug)}`;
      window.history.replaceState({}, "", nextUrl);
    }

    await openNote(notes[currentIndex], notes);
  } catch (error) {
    console.error(error);
    showError(
      "页面加载失败",
      "文章页初始化失败。请检查 <code>notes/notes.json</code> 是否存在且格式正确。"
    );
  }
}

init();
