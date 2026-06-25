# 高中数学复习系统

这是本地高中数学复习资料的总入口，包含二轮 Obsidian 题库、个人错题库、AI 笔记管理系统和《高考数学五年经典》题库。

建议先打开：

- [学习工作台](学习工作台.md)
- [互动工作台](学习工作台.html)
- [系统总控台](系统总控台.md)
- [内容优化总览](内容优化总览.md)
- [Open Design 方案](OPEN_DESIGN.md)
- [LLM 知识库](LLM知识库/README.md)
- [LLM Wiki 索引](LLM知识库/wiki/00_Index.md)
- [AI 学习流水线](Obsidian题库/08_AI笔记管理/AI学习流水线.md)
- [AI 对话导入清单](Obsidian题库/08_AI笔记管理/对话导入清单.md)
- [AI 笔记转化看板](Obsidian题库/08_AI笔记管理/AI笔记转化看板.md)
- [二轮 Obsidian 题库](Obsidian题库/README.md)
- [个人错题库](个人错题库/README.md)
- [高考数学五年经典](高考数学五年经典/README.md)

## 一键维护

在当前目录运行：

```powershell
.\tools\maintain_study_systems.ps1
```

它会刷新各题库进度、错题库统计、AI 笔记索引，编译 [LLM 知识库](LLM知识库/README.md)，并重新生成 [系统总控台](系统总控台.md)。
默认会并行运行互不冲突的维护任务；如果需要排查某个脚本，可以串行运行：

```powershell
.\tools\maintain_study_systems.ps1 --jobs 1
```

日常使用建议打开 [互动工作台](学习工作台.html)，它会汇总今日错题路线、题库进度、系统体检和常用入口。

内容层面的复习建议会同步生成到 [内容优化总览](内容优化总览.md) 和 [错题相似题推荐](个人错题库/00_控制台/相似题推荐.md)。

LLM 知识库采用“原始资料不可变 + LLM 持久 wiki + schema/日志/索引”的结构：从 [LLM Wiki 索引](LLM知识库/wiki/00_Index.md) 进入主题页和方法页；搜索本地编译索引可以运行：

```powershell
python .\tools\llm_wiki_maintain.py search "特征方程"
```

AI 对话学习流程：把每节导出的 `.md`/`.txt` 放进 [AI 对话导入入口](Obsidian题库/08_AI笔记管理/01_待整理/00_AI对话导入入口/README.md)，再按 [AI 学习流水线](Obsidian题库/08_AI笔记管理/AI学习流水线.md) 生成 DeepSeek 整理提示词。

如果已经知道 md/txt 的位置，也可以直接让系统导入并处理：

```powershell
.\tools\process_ai_material.ps1 "C:\path\to\一节课AI对话.md"
```

有 `DEEPSEEK_API_KEY` 或 `ANTHROPIC_AUTH_TOKEN` 时会直连整理；没有密钥时会自动生成 DeepSeek 提示词。
