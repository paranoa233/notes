# AI 学习流水线

本页是“听课/做题不会 -> 问 AI -> 导出对话 -> DeepSeek 整理 -> 标准笔记 -> 复习路线”的总入口。

## 固定流程

最省事的方式是在总目录直接处理指定文件：

```powershell
.\tools\process_ai_material.ps1 "C:\path\to\一节课AI对话.md"
```

有 `DEEPSEEK_API_KEY` 或 `ANTHROPIC_AUTH_TOKEN` 时会直连 DeepSeek v4 Pro 整理；没有密钥时会自动生成 prompt，等你手动交给 DeepSeek。

## 手动流程

1. 一节课、一个题组或一个明确卡点，只保留一个 AI 对话文件。
2. 把导出的 `.md` 或 `.txt` 放进 [[08_AI笔记管理/01_待整理/00_AI对话导入入口/README|AI对话导入入口]]。
3. 运行提示词生成：

```powershell
python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口
```

4. 打开 `04_运行记录/prompts` 里最新批次，把生成的 prompt 交给 DeepSeek v4 Pro，让它按标准笔记格式写入 `02_标准笔记`。每批次会有 `prompt_manifest.json` 记录来源文件。
5. 刷新索引：

```powershell
python tools/ai_note_manager.py index
```

6. 回到总目录运行：

```powershell
.\tools\maintain_study_systems.ps1
```

## 快捷入口

- [[08_AI笔记管理/对话导入清单|对话导入清单]]
- [[08_AI笔记管理/标准笔记索引|标准笔记索引]]
- [[08_AI笔记管理/AI笔记转化看板|AI笔记转化看板]]
- [[08_AI笔记管理/系统体检|系统体检]]
- [[08_AI笔记管理/90_模板/AI对话整理要求|AI对话整理要求]]
- [[08_AI笔记管理/90_模板/标准笔记模板|标准笔记模板]]
- [[00_控制台/AI笔记整理|控制台入口]]

## 对话导出命名

建议格式：

```text
10-3_数列特征根_2026-05-31_AI对话.md
1-1_基本不等式_2026-05-31_AI对话.md
```

文件名里尽量包含讲次、主题和日期。系统会从文件名、正文题号、正文关键词里辅助判断分类，但最终仍以 DeepSeek 整理出的 frontmatter 为准。

## 提示词去重

`prompts` 命令默认会跳过已经整理过的原始文件。确实需要重新生成时再加：

```powershell
python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口 --force
```

## 整理原则

- AI 对话只作为学习过程记录，不直接当标准答案。
- DeepSeek 输出的笔记要保留“用户卡点”和“下次怎么避免”，不要只写漂亮解法。
- 一节对话默认整理成一份本节主笔记。
- 如果对话里出现明确错题、稳定方法或待核对结论，先写进“待核对”，后续再拆成错题或方法卡。
- 整理完成后，系统会把标准笔记接入 [今日学习路线](../../个人错题库/00_控制台/今日学习路线.md) 和 [错题关联笔记](../../个人错题库/00_控制台/错题关联笔记.md)。
