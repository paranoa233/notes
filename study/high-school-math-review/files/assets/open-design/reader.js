(function () {
  const params = new URLSearchParams(window.location.search);
  const file = params.get("file") || "学习工作台.md";
  const content = document.getElementById("content");
  const status = document.getElementById("status");
  const toc = document.getElementById("toc");
  const prevButton = document.getElementById("prevProblem");
  const nextButton = document.getElementById("nextProblem");
  const focusButton = document.getElementById("focusToggle");
  const progress = document.getElementById("readerProgress");

  let problems = [];
  let activeProblemIndex = 0;
  let focusMode = false;

  function setStatus(message) {
    if (status) status.textContent = message;
  }

  function encodePath(path) {
    return encodeURI(path).replace(/#/g, "%23");
  }

  function decodePath(path) {
    try {
      return decodeURI(path);
    } catch (_) {
      return path;
    }
  }

  function dirname(path) {
    const index = path.lastIndexOf("/");
    return index >= 0 ? path.slice(0, index + 1) : "";
  }

  function joinPath(base, target) {
    if (/^(https?:)?\/\//.test(target) || target.startsWith("#") || target.startsWith("mailto:")) return target;
    if (target.startsWith("/")) return target.replace(/^\/+/, "");
    const stack = (base + target).split("/");
    const out = [];
    for (const part of stack) {
      if (!part || part === ".") continue;
      if (part === "..") out.pop();
      else out.push(part);
    }
    return out.join("/");
  }

  function readerHref(path) {
    return `reader.html?file=${encodeURIComponent(path)}`;
  }

  function slug(value, fallback) {
    const clean = String(value || "").trim().replace(/[^\w\u4e00-\u9fa5-]+/g, "-").replace(/^-+|-+$/g, "");
    return clean || fallback;
  }

  function preprocessMarkdown(text) {
    return text
      .replace(/^\uFEFF/, "")
      .replace(/^---[\s\S]*?---\s*/, "")
      .replace(/```dataview(?:js)?[\s\S]*?```/gmi, "")
      .replace(/^\s*>?\s*-?\s*(?:原PDF|原书PDF|章节PDF)：\[[^\]\r\n]+\]\((?:<file:\/\/\/[^>\r\n]+>|file:[^)]+|[^)\r\n]*)\)\s*$/gmi, "")
      .replace(/^\s*>\s*(?:讲义|题组|来源|原始题号|状态)：[^\r\n]*(?:\r?\n)?/gmi, "")
      .replace(/^\s*>\s*把文件名以本题编号开头的[^\r\n]*(?:\r?\n)?/gmi, "")
      .replace(/^\s*(?:source_pdf|source_pdf_uri|source_pdf_path|source_pdf_name|chapter_pdf|chapter_pdf_uri|chapter_pdf_path|chapter_pdf_name|source_line|generated_by):\s*["']?[^"\r\n]*["']?\s*$/gmi, "")
      .replace(/^\s*(?:\[\[00_控制台\/总览\|返回总览\]\]|题目目录：.*|原合集起始页：.*|原书起始页：.*)\s*$/gmi, "")
      .replace(/!\[\[([^\]]+\.(?:png|jpe?g|gif|webp|svg))\]\]/gi, "![]($1)")
      .replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, "[$2]($1)")
      .replace(/\[\[([^\]]+)\]\]/g, "[$1]($1)")
      .replace(/\n{3,}/g, "\n\n");
  }

  function escapeHtml(value) {
    return value.replace(/[&<>]/g, (char) => ({
      "&": "&amp;",
      "<": "&lt;",
      ">": "&gt;"
    })[char]);
  }

  function protectMath(text) {
    const store = [];
    const stash = (match) => {
      const token = `@@MATH_${store.length}@@`;
      store.push(escapeHtml(match));
      return token;
    };
    const protectedText = text
      .replace(/\$\$[\s\S]+?\$\$/g, stash)
      .replace(/\\\[[\s\S]+?\\\]/g, stash)
      .replace(/\\\([\s\S]+?\\\)/g, stash)
      .replace(/\$(?!\$)([^\n$]+?)\$/g, stash);
    return {
      text: protectedText,
      restore(html) {
        return html.replace(/@@MATH_(\d+)@@/g, (_, index) => store[Number(index)] || "");
      }
    };
  }

  function decorateRenderedLinks(baseDir) {
    content.querySelectorAll("a[href]").forEach((anchor) => {
      const href = anchor.getAttribute("href") || "";
      if (/^(https?:)?\/\//.test(href) || href.startsWith("mailto:")) {
        anchor.setAttribute("target", "_blank");
        anchor.setAttribute("rel", "noopener noreferrer");
        return;
      }
      const decodedHref = decodePath(href);
      if (decodedHref.endsWith(".md") || decodedHref.includes(".md#")) {
        const target = joinPath(baseDir, decodedHref);
        anchor.setAttribute("href", readerHref(target));
      } else if (!href.startsWith("#")) {
        anchor.setAttribute("href", encodePath(joinPath(baseDir, decodedHref)));
      }
    });

    content.querySelectorAll("img[src]").forEach((image) => {
      const src = image.getAttribute("src") || "";
      if (!/^(https?:)?\/\//.test(src)) {
        image.setAttribute("src", encodePath(joinPath(baseDir, decodePath(src))));
      }
    });
  }

  function previousLessonTitle(node) {
    let cursor = node.previousElementSibling;
    while (cursor) {
      if (cursor.tagName === "H2") return cursor.textContent.trim();
      cursor = cursor.previousElementSibling;
    }
    return "";
  }

  function isProblemHeading(heading) {
    return /^\d+(?:-\d+){2}\b/.test((heading.textContent || "").trim());
  }

  function structureProblems() {
    problems = [];
    const headings = [...content.querySelectorAll("h3")].filter(isProblemHeading);
    headings.forEach((heading, index) => {
      const section = document.createElement("section");
      const title = heading.textContent.trim();
      section.className = "reader-problem";
      section.dataset.problemIndex = String(index);
      section.dataset.title = title;
      section.dataset.lesson = previousLessonTitle(heading);
      heading.id = heading.id || slug(title, `problem-${index + 1}`);
      heading.classList.add("reader-problem-heading");
      heading.parentNode.insertBefore(section, heading);
      let cursor = heading;
      while (cursor) {
        const next = cursor.nextSibling;
        section.appendChild(cursor);
        if (next && next.nodeType === 1 && /^(H2|H3)$/i.test(next.tagName)) break;
        cursor = next;
      }
      problems.push({section, heading, title, lesson: section.dataset.lesson});
    });

    const hash = decodeURIComponent(location.hash.slice(1));
    const hashIndex = problems.findIndex((item) => item.heading.id === hash || item.title === hash);
    activeProblemIndex = hashIndex >= 0 ? hashIndex : 0;
  }

  function buildToc() {
    const headings = [...content.querySelectorAll("h2, h3")].slice(0, 28);
    if (!headings.length) {
      toc.innerHTML = "";
      return;
    }
    toc.innerHTML = `<div class="reader-toc-title">目录</div>` + headings.map((heading, index) => {
      const id = heading.id || `section-${index + 1}`;
      heading.id = id;
      return `<a href="#${id}" data-level="${heading.tagName === "H3" ? "3" : "2"}">${heading.textContent}</a>`;
    }).join("");
  }

  function updateProblemView(shouldScroll) {
    const hasProblems = problems.length > 0;
    if (prevButton) prevButton.disabled = !hasProblems || activeProblemIndex <= 0;
    if (nextButton) nextButton.disabled = !hasProblems || activeProblemIndex >= problems.length - 1;
    if (focusButton) {
      focusButton.disabled = !hasProblems;
      focusButton.setAttribute("aria-pressed", focusMode ? "true" : "false");
    }
    document.body.classList.toggle("reader-focus", focusMode && hasProblems);

    problems.forEach((item, index) => {
      item.section.classList.toggle("is-active", index === activeProblemIndex);
    });

    if (progress) {
      if (!hasProblems) {
        progress.textContent = "";
      } else {
        const item = problems[activeProblemIndex];
        const lesson = item.lesson ? `${item.lesson} · ` : "";
        progress.textContent = `${activeProblemIndex + 1}/${problems.length} · ${lesson}${item.title}`;
      }
    }

    if (shouldScroll && hasProblems) {
      problems[activeProblemIndex].section.scrollIntoView({behavior: "smooth", block: "start"});
      history.replaceState(null, "", `#${problems[activeProblemIndex].heading.id}`);
    }
  }

  function setActiveProblem(index, shouldScroll = true) {
    if (!problems.length) return;
    activeProblemIndex = Math.max(0, Math.min(problems.length - 1, index));
    updateProblemView(shouldScroll);
  }

  function bindReaderControls() {
    if (prevButton) prevButton.addEventListener("click", () => setActiveProblem(activeProblemIndex - 1));
    if (nextButton) nextButton.addEventListener("click", () => setActiveProblem(activeProblemIndex + 1));
    if (focusButton) {
      focusButton.addEventListener("click", () => {
        focusMode = !focusMode;
        updateProblemView(true);
      });
    }
    window.addEventListener("keydown", (event) => {
      const tag = document.activeElement && document.activeElement.tagName;
      if (!focusMode || /^(INPUT|TEXTAREA|SELECT)$/i.test(tag || "")) return;
      if (event.key === "ArrowRight") {
        event.preventDefault();
        setActiveProblem(activeProblemIndex + 1);
      }
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        setActiveProblem(activeProblemIndex - 1);
      }
    });
  }

  async function render() {
    if (/^(https?:)?\/\//.test(file)) {
      throw new Error("阅读器只打开当前站点内的 Markdown 文件。");
    }
    const response = await fetch(encodePath(file), {cache: "no-store"});
    if (!response.ok) throw new Error(`无法读取文件：${response.status} ${response.statusText}`);
    const markdown = protectMath(preprocessMarkdown(await response.text()));
    const md = window.markdownit({
      html: true,
      linkify: false,
      typographer: true,
      breaks: false
    });
    content.innerHTML = markdown.restore(md.render(markdown.text));
    decorateRenderedLinks(dirname(file));
    structureProblems();
    buildToc();
    setStatus("Markdown 已渲染，正在排版公式...");
    if (window.renderMathInElement) {
      window.renderMathInElement(content, {
        delimiters: [
          {left: "$$", right: "$$", display: true},
          {left: "\\[", right: "\\]", display: true},
          {left: "\\(", right: "\\)", display: false},
          {left: "$", right: "$", display: false}
        ],
        ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
        throwOnError: false,
        strict: "ignore",
        trust: false
      });
      setStatus("");
    } else {
      setStatus("Markdown 已渲染；KaTeX 未加载，公式会保留为 TeX");
    }
    updateProblemView(false);
    document.title = `${file.split("/").pop()} - 题库阅读器`;
  }

  window.addEventListener("DOMContentLoaded", () => {
    bindReaderControls();
    render().catch((error) => {
      setStatus(error.message);
      content.innerHTML = `<h1>打开失败</h1><p>${error.message}</p>`;
      updateProblemView(false);
    });
  });
})();
