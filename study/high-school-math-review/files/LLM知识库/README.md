# LLM 知识库

这是在现有题库、错题库和 AI 笔记之上新增的持久 wiki 层。它借鉴 Karpathy 的 LLM-Wiki 思路：原始资料保持可追溯，LLM 负责把材料持续编译成更容易检索、复习和迁移的知识页。

## 入口

- [Wiki 首页](wiki/00_Index.md)
- [系统概览](wiki/01_Overview.md)
- [今日学习闭环](wiki/02_Learning_Loop.md)
- [资料源注册表](wiki/03_Source_Registry.md)
- [健康检查](wiki/04_Health_Check.md)
- [待编译队列](wiki/05_Compile_Queue.md)
- [操作规约](SCHEMA.md)

## 当前快照

- 题库题目：2603
- 错题：2
- AI 标准笔记：2
- 主题页：201
- 方法页：16
- 检查项：3

## 维护

```powershell
.\tools\maintain_study_systems.ps1
```

或只重建这一层：

```powershell
python .\tools\llm_wiki_maintain.py refresh
```
