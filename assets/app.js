const SITE_TITLE = "paranoa233's notes";
const DEFAULT_DESCRIPTION =
  "一个以黑白灰为主、适合长期整理 Markdown 与公式的笔记站。";

const state = {
  notes: [],
  keyword: "",
  activeTag: "all",
  currentSlug: ""
};

const elements = {
  searchInput: document.getElementById("search-input"),
  tagList: document.getElementById("tag-list"),
  noteList: document.getElementById("note-list"),
  noteCount: document.getElementById("note-count"),
  activeNoteDate: document.getElementById("active-note-date"),
  articleDate: document.getElementById("article-date"),
  articleTitle: document.getElementById("article-title"),
  article: document.getElementById("article"),
  articleTags: document.getElementById("article-tags"),
  articleNav: document.getElementById("article-nav"),
  metaDescription: document.querySelector('meta[name="description"]'),
  content: document.querySelector(".content")
};

marked.setOptions({
  breaks: true,
  gfm: true
});

function normalize(text = "") {
  return text.toLowerCase().trim();
}

function getHashSlug() {
  return decodeURIComponent(location.hash.replace(/^#\/?/, ""));
}

function getFilteredNotes() {
  const keyword = normalize(state.keyword);

  return state.notes.filter((note) => {
    const matchesTag =
      state.activeTag === "all" || note.tags.includes(state.activeTag);

    if (!keyword) {
      return matchesTag;
    }

    const haystack = normalize(
      [note.title, note.summary, note.date, note.tags.join(" ")].join(" ")
    );

    return matchesTag && haystack.includes(keyword);
  });
}

function getNoteBySlug(slug) {
  return state.notes.find((note) => note.slug === slug);
}

function setPageMeta(note) {
  document.title = note ? `${note.title} | ${SITE_TITLE}` : SITE_TITLE;

  if (elements.metaDescription) {
    elements.metaDescription.content = note?.summary || DEFAULT_DESCRIPTION;
  }
}

function renderTags() {
  const tags = new Set(["all"]);
  state.notes.forEach((note) => note.tags.forEach((tag) => tags.add(tag)));

  elements.tagList.innerHTML = "";

  Array.from(tags).forEach((tag) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `tag-chip${tag === state.activeTag ? " is-active" : ""}`;
    button.textContent = tag === "all" ? "全部" : tag;
    button.addEventListener("click", () => {
      state.activeTag = tag;
      renderTags();
      renderNoteList();
    });
    elements.tagList.appendChild(button);
  });
}

function renderNoteList() {
  const filteredNotes = getFilteredNotes();
  elements.noteCount.textContent = `${filteredNotes.length} 篇`;

  if (!filteredNotes.length) {
    elements.noteList.innerHTML =
      '<div class="empty-state">没有匹配的笔记，换个关键词或标签试试。</div>';
    elements.activeNoteDate.textContent = "";
    return;
  }

  const shouldSwitch =
    !filteredNotes.some((note) => note.slug === state.currentSlug);

  if (shouldSwitch) {
    const nextSlug = filteredNotes[0].slug;
    state.currentSlug = nextSlug;
    if (getHashSlug() !== nextSlug) {
      location.hash = `/${encodeURIComponent(nextSlug)}`;
      return;
    }
  }

  elements.noteList.innerHTML = "";

  filteredNotes.forEach((note) => {
    const link = document.createElement("a");
    link.href = `#/${encodeURIComponent(note.slug)}`;
    link.className = `note-card${note.slug === state.currentSlug ? " is-active" : ""}`;

    const title = document.createElement("strong");
    title.textContent = note.title;

    const summary = document.createElement("p");
    summary.textContent = note.summary;

    const date = document.createElement("span");
    date.textContent = note.date;

    link.append(title, summary, date);
    elements.noteList.appendChild(link);
  });

  const activeNote = getNoteBySlug(state.currentSlug);
  elements.activeNoteDate.textContent = activeNote ? activeNote.date : "";
}

function renderArticleTags(note) {
  elements.articleTags.innerHTML = "";
  note.tags.forEach((tag) => {
    const span = document.createElement("span");
    span.className = "article-tag";
    span.textContent = tag;
    elements.articleTags.appendChild(span);
  });
}

function renderArticleNav(filteredNotes, currentIndex) {
  if (currentIndex < 0) {
    elements.articleNav.innerHTML = "";
    return;
  }

  const previous = filteredNotes[currentIndex - 1];
  const next = filteredNotes[currentIndex + 1];

  elements.articleNav.innerHTML = "";

  if (previous) {
    const prevLink = document.createElement("a");
    prevLink.className = "nav-link";
    prevLink.href = `#/${encodeURIComponent(previous.slug)}`;
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
    nextLink.href = `#/${encodeURIComponent(next.slug)}`;
    const nextLabel = document.createElement("span");
    nextLabel.textContent = "下一篇";
    const nextTitle = document.createElement("strong");
    nextTitle.textContent = next.title;
    nextLink.append(nextLabel, nextTitle);
    elements.articleNav.appendChild(nextLink);
  }
}

async function openNote(slug, options = {}) {
  const { scrollToArticle = false } = options;
  const note = getNoteBySlug(slug);
  if (!note) {
    setPageMeta();
    elements.articleTitle.textContent = "未找到笔记";
    elements.articleDate.textContent = "";
    elements.articleTags.innerHTML = "";
    elements.articleNav.innerHTML = "";
    elements.article.innerHTML =
      '<div class="empty-state">没有找到这篇笔记，请检查链接是否正确。</div>';
    return;
  }

  state.currentSlug = note.slug;
  renderNoteList();
  renderArticleTags(note);
  elements.articleTitle.textContent = note.title;
  elements.articleDate.textContent = note.date || "";
  setPageMeta(note);

  try {
    const response = await fetch(`./notes/${note.file}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const markdown = await response.text();
    const rendered = marked.parse(markdown);

    if (window.MathJax?.typesetClear) {
      window.MathJax.typesetClear([elements.article]);
    }

    elements.article.innerHTML = DOMPurify.sanitize(rendered, {
      USE_PROFILES: { html: true }
    });

    if (window.MathJax?.typesetPromise) {
      await window.MathJax.typesetPromise([elements.article]);
    }

    const filteredNotes = getFilteredNotes();
    const currentIndex = filteredNotes.findIndex((item) => item.slug === slug);
    renderArticleNav(filteredNotes, currentIndex);

    if (scrollToArticle && window.matchMedia("(max-width: 1080px)").matches) {
      elements.content?.scrollIntoView({
        behavior: "smooth",
        block: "start"
      });
    }
  } catch (error) {
    console.error(error);
    elements.article.innerHTML = `
      <div class="empty-state">
        读取笔记失败了。请确认 <code>notes/${note.file}</code> 存在并已推送到 GitHub。
      </div>
    `;
  }
}

function bindEvents() {
  elements.searchInput.addEventListener("input", (event) => {
    state.keyword = event.target.value;
    renderNoteList();

    const filteredNotes = getFilteredNotes();
    if (filteredNotes.length && !filteredNotes.some((note) => note.slug === state.currentSlug)) {
      location.hash = `/${encodeURIComponent(filteredNotes[0].slug)}`;
    }
  });

  window.addEventListener("hashchange", () => {
    const slug = getHashSlug() || state.notes[0]?.slug;
    if (slug) {
      const shouldScroll = Boolean(state.currentSlug) && state.currentSlug !== slug;
      openNote(slug, { scrollToArticle: shouldScroll });
    }
  });
}

async function init() {
  bindEvents();
  setPageMeta();

  try {
    const response = await fetch("./notes/notes.json");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    state.notes = await response.json();
    renderTags();

    const firstSlug = getHashSlug() || state.notes[0]?.slug;
    if (!firstSlug) {
      setPageMeta();
      elements.articleTitle.textContent = "还没有笔记";
      elements.articleDate.textContent = "";
      elements.articleTags.innerHTML = "";
      elements.articleNav.innerHTML = "";
      elements.article.innerHTML =
        '<div class="empty-state">还没有笔记。先在 <code>notes/notes.json</code> 里登记一篇吧。</div>';
      return;
    }

    if (!location.hash) {
      location.hash = `/${encodeURIComponent(firstSlug)}`;
      return;
    }

    openNote(firstSlug);
  } catch (error) {
    console.error(error);
    setPageMeta();
    elements.articleTitle.textContent = "站点初始化失败";
    elements.articleDate.textContent = "";
    elements.articleTags.innerHTML = "";
    elements.articleNav.innerHTML = "";
    elements.article.innerHTML = `
      <div class="empty-state">
        站点初始化失败。请检查 <code>notes/notes.json</code> 是否存在且格式正确。
      </div>
    `;
  }
}

init();
