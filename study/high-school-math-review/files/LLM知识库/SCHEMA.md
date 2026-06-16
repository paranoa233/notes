# LLM 知识库操作规约

## 核心原则

1. 原始资料不直接改写：题库、PDF、错题原文和 AI 对话归档是 source-of-truth。
2. Wiki 是编译层：主题页、方法页、学习闭环和健康检查可以反复生成。
3. 每个结论都要能追回来源：优先链接到错题、标准笔记、题目页或控制台数据。
4. LLM 的价值不是堆摘要，而是维护结构：分类、命名、链接、待办、薄弱点和迁移路线。

## 目录角色

| 目录 | 角色 | 写入策略 |
| --- | --- | --- |
| `Obsidian题库` | 二轮题库 source-of-truth | 只通过原维护脚本和导入脚本更新 |
| `高考数学五年经典` | 五年经典题库 source-of-truth | 只通过原维护脚本和解答导入脚本更新 |
| `个人错题库` | 个人错题和复习状态 source-of-truth | 新错题按模板进入，复习后更新状态字段 |
| `Obsidian题库/08_AI笔记管理/02_标准笔记` | 标准方法卡和知识卡 | 由 AI 对话/错题复盘整理后写入 |
| `LLM知识库/wiki` | LLM 编译出的持久 wiki | 可由 `llm_wiki_maintain.py` 重建 |

## LLM 工作流

1. 先读 `LLM知识库/wiki/00_Index.md`，再进入相关主题页或方法页。
2. 回答题目或复习问题时，至少链接一个源文件：错题、题目或标准笔记。
3. 发现重复错因时，优先补一张标准笔记，再让维护脚本重新编译。
4. 发现分类不确定时，把置信度写低，并在健康检查中暴露给人工确认。
5. 新材料先进入导入入口，不把聊天记录直接混进标准笔记区。

## 推荐字段

错题页应至少维护：`wrong_id`、`source_problem_id`、`lesson_id`、`module`、`topic`、`priority`、`status`、`mastery`、`wrong_reason`、`knowledge_points`、`methods`、`anti_mistake_tip`、`last_review`、`next_review`。

标准笔记应至少维护：`note_id`、`note_kind`、`status`、`title`、`lesson_id`、`module`、`topic`、`classification_confidence`、`related_problem_ids`、`knowledge_points`、`methods`、`quality_flags`。

## 复习闭环定义

错题重做 -> 标准笔记复盘 -> 二轮同类题 -> 五年经典迁移题 -> 更新错题状态。
