# AI 对话导入入口

把每节学习导出的 AI 对话放在这里。来源工具不限，只要是 `.md`、`.markdown` 或 `.txt`。

## 建议规则

- 一节课或一个题组一个文件。
- 文件名包含讲次、主题和日期。
- 不要把多个不相干专题塞进同一个文件。
- 导出后不要在原文件里反复改内容；需要补充时另开一个同主题追加文件。

## 下一步

在总目录直接处理指定文件：

```powershell
.\tools\process_ai_material.ps1 "C:\path\to\一节课AI对话.md"
```

或者在 `Obsidian题库` 目录运行：

```powershell
python tools/ai_note_manager.py intake
python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口
```

生成的提示词会在 `04_运行记录/prompts` 里。
