const BUILD_ID = "20260413-3";

const state = {
  notes: [],
  keyword: "",
  activeTag: "all"
};

const elements = {
  searchInput: document.getElementById("search-input"),
  tagList: document.getElementById("tag-list"),
  noteList: document.getElementById("note-list"),
  noteCount: document.getElementById("note-count"),
  collectionList: document.getElementById("collection-list"),
  collectionCount: document.getElementById("collection-count")
};

function normalize(text = "") {
  return text.toLowerCase().trim();
}

function isHomeVisible(note) {
  return note.home !== false;
}

function getVisibleNotes() {
  return state.notes.filter(isHomeVisible);
}

function getFilteredNotes() {
  const keyword = normalize(state.keyword);
  const notes = getVisibleNotes();

  return notes.filter((note) => {
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
  getVisibleNotes().forEach((note) =>
    note.tags.forEach((tag) => tags.add(tag))
  );

  elements.tagList.innerHTML = "";
  Array.from(tags).forEach((tag) => {
    elements.tagList.appendChild(createTagChip(tag));
  });
}

function getCollections() {
  const groups = [];
  const lookup = new Map();

  state.notes.forEach((note) => {
    if (!note.collectionId) {
      return;
    }

    if (!lookup.has(note.collectionId)) {
      const group = { id: note.collectionId, notes: [] };
      lookup.set(note.collectionId, group);
      groups.push(group);
    }

    lookup.get(note.collectionId).notes.push(note);
  });

  return groups
    .map((group) => {
      const overview =
        group.notes.find((note) => note.collectionRole === "overview") ||
        group.notes[0];
      const sections = group.notes
        .filter((note) => note.collectionRole === "section")
        .sort((left, right) => {
          const leftOrder = left.collectionOrder ?? left.sectionNumber ?? 0;
          const rightOrder = right.collectionOrder ?? right.sectionNumber ?? 0;
          return leftOrder - rightOrder;
        });

      return { ...group, overview, sections };
    })
    .filter((group) => group.overview && group.sections.length);
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

function createCollectionCard(collection, isInitiallyOpen) {
  const details = document.createElement("details");
  details.className = "collection-card";
  details.open = isInitiallyOpen;

  const summary = document.createElement("summary");
  summary.className = "collection-summary";

  const summaryMain = document.createElement("div");
  summaryMain.className = "collection-summary-main";

  const title = document.createElement("h3");
  title.className = "collection-title";
  title.textContent = collection.overview.title;

  const description = document.createElement("p");
  description.className = "collection-description";
  description.textContent = collection.overview.summary;

  const count = document.createElement("span");
  count.className = "collection-count-badge";
  count.textContent = `${
    collection.sections.length
  } ${collection.overview.collectionUnit || "节"}`;

  summaryMain.append(title, description);
  summary.append(summaryMain, count);

  const body = document.createElement("div");
  body.className = "collection-body";

  const overviewLink = document.createElement("a");
  overviewLink.className = "collection-overview-link";
  overviewLink.href = `./note.html?slug=${encodeURIComponent(
    collection.overview.slug
  )}`;
  overviewLink.textContent = "打开导读页";

  const sectionList = document.createElement("div");
  sectionList.className = "collection-sections";

  collection.sections.forEach((note) => {
    const link = document.createElement("a");
    link.className = "collection-section-link";
    link.href = `./note.html?slug=${encodeURIComponent(note.slug)}`;

    const index = document.createElement("span");
    index.className = "collection-section-index";
    index.textContent = note.collectionLabel || `§${note.sectionNumber}`;

    const text = document.createElement("span");
    text.className = "collection-section-text";
    text.textContent =
      note.collectionTitle || note.title.replace(/^§\d+\s*/, "");

    link.append(index, text);
    sectionList.appendChild(link);
  });

  body.append(overviewLink, sectionList);
  details.append(summary, body);

  return details;
}

function renderCollections() {
  const collections = getCollections();
  elements.collectionCount.textContent = `${collections.length} 部`;

  if (!collections.length) {
    elements.collectionList.innerHTML =
      '<div class="empty-state">这里还没有专题书籍。</div>';
    return;
  }

  elements.collectionList.innerHTML = "";
  collections.forEach((collection, index) => {
    elements.collectionList.appendChild(
      createCollectionCard(collection, index === 0)
    );
  });
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
    const response = await fetch(`./notes/notes.json?v=${BUILD_ID}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    state.notes = await response.json();
    renderTags();
    renderCollections();
    renderNoteList();
  } catch (error) {
    console.error(error);
    elements.noteList.innerHTML =
      '<div class="empty-state">主页加载失败。请检查 <code>notes/notes.json</code> 是否存在且格式正确。</div>';
    elements.noteCount.textContent = "0 篇";
    elements.collectionList.innerHTML =
      '<div class="empty-state">专题书架加载失败。</div>';
    elements.collectionCount.textContent = "0 部";
  }
}

init();
