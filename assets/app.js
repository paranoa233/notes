const state = {
  notes: [],
  keyword: "",
  activeTag: "all"
};

const elements = {
  searchInput: document.getElementById("search-input"),
  tagList: document.getElementById("tag-list"),
  noteList: document.getElementById("note-list"),
  noteCount: document.getElementById("note-count")
};

function normalize(text = "") {
  return text.toLowerCase().trim();
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

function createTagChip(tag) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = `tag-chip${tag === state.activeTag ? " is-active" : ""}`;
  button.textContent = tag === "all" ? "全部" : tag;
  button.addEventListener("click", () => {
    state.activeTag = tag;
    renderTags();
    renderNoteList();
  });
  return button;
}

function renderTags() {
  const tags = new Set(["all"]);
  state.notes.forEach((note) => note.tags.forEach((tag) => tags.add(tag)));

  elements.tagList.innerHTML = "";
  Array.from(tags).forEach((tag) => {
    elements.tagList.appendChild(createTagChip(tag));
  });
}

function createNoteCard(note) {
  const link = document.createElement("a");
  link.href = `./note.html?slug=${encodeURIComponent(note.slug)}`;
  link.className = "note-card";

  const title = document.createElement("h3");
  title.className = "note-card-title";
  title.textContent = note.title;

  const summary = document.createElement("p");
  summary.className = "note-card-summary";
  summary.textContent = note.summary;

  const meta = document.createElement("div");
  meta.className = "note-card-meta";

  const date = document.createElement("span");
  date.textContent = note.date;

  const tagWrap = document.createElement("div");
  tagWrap.className = "note-card-tags";
  note.tags.forEach((tag) => {
    const tagItem = document.createElement("span");
    tagItem.className = "note-mini-tag";
    tagItem.textContent = tag;
    tagWrap.appendChild(tagItem);
  });

  meta.append(date, tagWrap);
  link.append(title, summary, meta);

  return link;
}

function renderNoteList() {
  const filteredNotes = getFilteredNotes();
  elements.noteCount.textContent = `${filteredNotes.length} 篇`;

  if (!filteredNotes.length) {
    elements.noteList.innerHTML =
      '<div class="empty-state">没有匹配的文章，换个关键词或标签试试。</div>';
    return;
  }

  elements.noteList.innerHTML = "";
  filteredNotes.forEach((note) => {
    elements.noteList.appendChild(createNoteCard(note));
  });
}

function bindEvents() {
  elements.searchInput.addEventListener("input", (event) => {
    state.keyword = event.target.value;
    renderNoteList();
  });
}

async function init() {
  bindEvents();

  try {
    const response = await fetch("./notes/notes.json");
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    state.notes = await response.json();
    renderTags();
    renderNoteList();
  } catch (error) {
    console.error(error);
    elements.noteList.innerHTML =
      '<div class="empty-state">主页加载失败。请检查 <code>notes/notes.json</code> 是否存在且格式正确。</div>';
    elements.noteCount.textContent = "0 篇";
  }
}

init();
