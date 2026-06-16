# Agent Guide

This workspace is a high-school math review system with a generated LLM wiki layer.

Before making study-system changes or answering content questions from this repository:

1. Read `LLM知识库/SCHEMA.md` for the source-of-truth and wiki rules.
2. Start from `LLM知识库/wiki/00_Index.md`.
3. Use topic pages under `LLM知识库/wiki/topics/` and method pages under `LLM知识库/wiki/methods/` as compiled navigation, then verify against the linked source notes.
4. Treat these as source-of-truth areas:
   - `Obsidian题库`
   - `高考数学五年经典`
   - `个人错题库`
   - `Obsidian题库/08_AI笔记管理/02_标准笔记`
5. Treat `LLM知识库/wiki` as generated/compiled output. Prefer updating the underlying source notes or `tools/llm_wiki_maintain.py`, then refresh the wiki.

Useful commands:

```powershell
.\tools\maintain_study_systems.ps1
python .\tools\llm_wiki_maintain.py search "特征方程"
```
