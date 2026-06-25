(function () {
  const params = new URLSearchParams(window.location.search);
  const file = params.get("file") || "学习工作台.md";
  const content = document.getElementById("content");
  const status = document.getElementById("status");
  const filePath = document.getElementById("filePath");
  const rawLink = document.getElementById("rawLink");
  const toc = document.getElementById("toc");

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

  function preprocessMarkdown(text) {
    return text
      .replace(/^\uFEFF/, "")
      .replace(/^---[\s\S]*?---\s*/, "")
      .replace(/^\s*>?\s*-?\s*\u539fPDF：\[\u6253\u5f00\u5b66\u751f\u7248PDF\]\(<file:\/\/\/[^>\r\n]+>\)\s*$/gmi, "")
      .replace(/^\s*>?\s*-?\s*(?:\u539f\u4e66PDF|\u7ae0\u8282PDF)：\[[^\]\r\n]+PDF\]\((?:<file:\/\/\/[^>\r\n]+>|\s*)\)\s*$/gmi, "")
      .replace(/^\s*(?:source_pdf|source_pdf_uri|source_pdf_path|chapter_pdf_uri|chapter_pdf_path):\s*["']?(?:file:\/\/\/|[A-Za-z]:[\\/]|\\\\)[^\r\n]*$/gmi, "")
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

  function buildToc() {
    const headings = [...content.querySelectorAll("h2, h3")].slice(0, 24);
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

  async function render() {
    if (/^(https?:)?\/\//.test(file)) {
      throw new Error("阅读器只打开当前站点内的 Markdown 文件。");
    }
    filePath.textContent = file;
    rawLink.href = encodePath(file);
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
    buildToc();
    status.textContent = "Markdown 已渲染，正在排版公式...";
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
      status.textContent = "公式渲染完成";
    } else {
      status.textContent = "Markdown 已渲染；KaTeX 未加载，公式会保留为 TeX";
    }
    document.title = `${file.split("/").pop()} - 题库阅读器`;
  }

  window.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("[data-reader-link]").forEach((anchor) => {
      const href = anchor.getAttribute("href") || "";
      if (href.endsWith(".md")) anchor.setAttribute("href", readerHref(href));
    });
    render().catch((error) => {
      status.textContent = error.message;
      content.innerHTML = `<h1>打开失败</h1><p>${error.message}</p>`;
    });
  });
})();
