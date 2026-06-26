(function () {
  const state = {
    index: null,
    query: "",
    method: "",
    bank: "",
    module: "",
    kind: "",
    sort: "method"
  };

  const els = {
    heroStats: document.getElementById("heroStats"),
    query: document.getElementById("queryInput"),
    method: document.getElementById("methodSelect"),
    bank: document.getElementById("bankSelect"),
    module: document.getElementById("moduleSelect"),
    kind: document.getElementById("kindSelect"),
    sort: document.getElementById("sortSelect"),
    chips: document.getElementById("methodChips"),
    count: document.getElementById("resultCount"),
    list: document.getElementById("resultList")
  };

  function h(value) {
    return String(value ?? "").replace(/[&<>"']/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;",
      '"': "&quot;",
      "'": "&#39;"
    })[char]);
  }

  function normalize(value) {
    return String(value || "").replace(/\s+/g, "").toLowerCase();
  }

  function readerHref(path) {
    return `reader.html?file=${encodeURIComponent(path)}`;
  }

  function option(value, label) {
    return `<option value="${h(value)}">${h(label)}</option>`;
  }

  function uniqueSorted(items) {
    return [...new Set(items.filter(Boolean))].sort((a, b) => String(a).localeCompare(String(b), "zh-CN"));
  }

  function initFromUrl() {
    const params = new URLSearchParams(window.location.search);
    state.query = params.get("q") || "";
    state.method = params.get("method") || "";
    state.bank = params.get("bank") || "";
    state.module = params.get("module") || "";
    state.kind = params.get("kind") || "";
    state.sort = params.get("sort") || "method";
  }

  function writeUrl() {
    const params = new URLSearchParams();
    for (const key of ["query", "method", "bank", "module", "kind", "sort"]) {
      const paramKey = key === "query" ? "q" : key;
      if (state[key]) params.set(paramKey, state[key]);
    }
    const next = `${location.pathname}${params.toString() ? `?${params}` : ""}`;
    history.replaceState(null, "", next);
  }

  function hydrateControls() {
    const index = state.index;
    const problems = index.problems || [];
    const methods = Object.entries(index.methods || {})
      .filter(([name]) => name !== "未标注")
      .sort((a, b) => Number(b[1]) - Number(a[1]));
    const kinds = Object.entries(index.kinds || {})
      .filter(([name]) => name !== "未标注")
      .sort((a, b) => Number(b[1]) - Number(a[1]));
    els.method.innerHTML = option("", "全部") + methods.map(([name, count]) => option(name, `${name} · ${count}`)).join("");
    els.module.innerHTML = option("", "全部") + uniqueSorted(problems.map((item) => item.module)).map((name) => option(name, name)).join("");
    els.kind.innerHTML = option("", "全部") + kinds.map(([name, count]) => option(name, `${name} · ${count}`)).join("");

    els.query.value = state.query;
    els.method.value = state.method;
    els.bank.value = state.bank;
    els.module.value = state.module;
    els.kind.value = state.kind;
    els.sort.value = state.sort;

    els.heroStats.innerHTML = [
      ["题量", index.total || 0],
      ["方法", methods.length],
      ["专题", Object.keys(index.modules || {}).length]
    ].map(([label, value]) => `<div class="stat"><b>${h(value)}</b><span>${h(label)}</span></div>`).join("");

    els.chips.innerHTML = methods.map(([name, count]) =>
      `<button class="chip${name === state.method ? " active" : ""}" type="button" data-method="${h(name)}">${h(name)}<small>${h(count)}</small></button>`
    ).join("");
  }

  function matches(item) {
    if (state.bank && item.bankId !== state.bank) return false;
    if (state.method && !(item.methods || []).includes(state.method)) return false;
    if (state.module && item.module !== state.module) return false;
    if (state.kind && item.kind !== state.kind) return false;
    const query = normalize(state.query);
    if (!query) return true;
    const text = normalize([
      item.problemId,
      item.lessonId,
      item.lessonTitle,
      item.module,
      item.topic,
      item.section,
      item.kind,
      item.excerpt,
      (item.methods || []).join(" ")
    ].join(" "));
    return text.includes(query);
  }

  function sortResults(items) {
    const collator = new Intl.Collator("zh-CN", {numeric: true});
    const byProblem = (a, b) => collator.compare(String(a.problemId), String(b.problemId));
    if (state.sort === "bank") {
      return items.sort((a, b) => collator.compare(a.bank, b.bank) || byProblem(a, b));
    }
    if (state.sort === "module") {
      return items.sort((a, b) => collator.compare(a.module, b.module) || collator.compare(a.lessonId, b.lessonId) || byProblem(a, b));
    }
    return items.sort((a, b) => {
      const aHit = state.method && (a.methods || []).includes(state.method) ? 0 : 1;
      const bHit = state.method && (b.methods || []).includes(state.method) ? 0 : 1;
      return aHit - bHit || collator.compare(a.module, b.module) || byProblem(a, b);
    });
  }

  function renderResults() {
    const all = state.index.problems || [];
    const results = sortResults(all.filter(matches));
    const visible = results.slice(0, 120);
    els.count.textContent = results.length > 120 ? `${results.length} 题，显示前 120 题` : `${results.length} 题`;
    if (!visible.length) {
      els.list.innerHTML = `<div class="empty">没有匹配题目。</div>`;
      return;
    }
    els.list.innerHTML = visible.map((item) => {
      const tags = (item.methods || []).slice(0, 5).map((name) => `<span class="tag">${h(name)}</span>`).join("");
      const title = `${item.problemId} ${item.lessonTitle || item.topic || ""}`.trim();
      return `<article class="result-card">
        <div class="result-title">
          <a href="${h(readerHref(item.file))}">${h(title)}</a>
          <span class="bank">${h(item.bank)}</span>
        </div>
        <div class="meta">${h([item.module, item.topic, item.section, item.kind].filter(Boolean).join(" / "))}</div>
        <div class="excerpt">${h(item.excerpt || "")}</div>
        <div class="tags">${tags || `<span class="tag">未标注</span>`}</div>
      </article>`;
    }).join("");
  }

  function render() {
    hydrateControls();
    renderResults();
    writeUrl();
  }

  function bindControls() {
    els.query.addEventListener("input", () => {
      state.query = els.query.value.trim();
      renderResults();
      writeUrl();
    });
    for (const [key, element] of [["method", els.method], ["bank", els.bank], ["module", els.module], ["kind", els.kind], ["sort", els.sort]]) {
      element.addEventListener("change", () => {
        state[key] = element.value;
        render();
      });
    }
    els.chips.addEventListener("click", (event) => {
      const button = event.target.closest("[data-method]");
      if (!button) return;
      state.method = button.dataset.method === state.method ? "" : button.dataset.method;
      render();
    });
  }

  async function boot() {
    initFromUrl();
    bindControls();
    const response = await fetch("assets/open-design/question-search-index.json?v=20260626-2", {cache: "no-store"});
    if (!response.ok) throw new Error(`索引加载失败：${response.status}`);
    state.index = await response.json();
    render();
  }

  boot().catch((error) => {
    els.count.textContent = "";
    els.list.innerHTML = `<div class="empty">${h(error.message)}</div>`;
  });
})();
