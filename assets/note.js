const SITE_TITLE = "paranoa233's notes";
const DEFAULT_DESCRIPTION =
  "paranoa233 的独立文章阅读页，采用白纸黑字的阅读模式。";

const elements = {
  articleDate: document.getElementById("article-date"),
  articleTitle: document.getElementById("article-title"),
  articleTags: document.getElementById("article-tags"),
  article: document.getElementById("article"),
  articleNav: document.getElementById("article-nav"),
  metaDescription: document.querySelector('meta[name="description"]')
};

marked.setOptions({
  breaks: true,
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

function renderArticleNav(notes, currentIndex) {
  elements.articleNav.innerHTML = "";

  const previous = notes[currentIndex - 1];
  const next = notes[currentIndex + 1];

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

function showError(title, message) {
  setPageMeta();
  elements.articleTitle.textContent = title;
  elements.articleDate.textContent = "";
  elements.articleTags.innerHTML = "";
  elements.articleNav.innerHTML = "";
  elements.article.innerHTML = `<div class="empty-state">${message}</div>`;
}

async function openNote(note, notes, currentIndex) {
  elements.articleTitle.textContent = note.title;
  elements.articleDate.textContent = note.date || "";
  renderTags(note);
  setPageMeta(note);
  renderArticleNav(notes, currentIndex);

  try {
    const response = await fetch(`./notes/${note.file}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const markdown = await response.text();
    const cleanedMarkdown = stripLeadingTitle(markdown, note.title);
    const rendered = marked.parse(cleanedMarkdown);

    if (window.MathJax?.typesetClear) {
      window.MathJax.typesetClear([elements.article]);
    }

    elements.article.innerHTML = DOMPurify.sanitize(rendered, {
      USE_PROFILES: { html: true }
    });

    if (window.MathJax?.typesetPromise) {
      await window.MathJax.typesetPromise([elements.article]);
    }
  } catch (error) {
    console.error(error);
    elements.article.innerHTML =
      '<div class="empty-state">文章读取失败。请确认对应的 Markdown 文件已经存在并成功推送。</div>';
  }
}

async function init() {
  try {
    const response = await fetch("./notes/notes.json");
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

    await openNote(notes[currentIndex], notes, currentIndex);
  } catch (error) {
    console.error(error);
    showError(
      "页面加载失败",
      "文章页初始化失败。请检查 <code>notes/notes.json</code> 是否存在且格式正确。"
    );
  }
}

init();
