# AI 笔记管理系统

这个区域用来把每节 AI 对话、草稿笔记、题解复盘整理成统一格式的 Obsidian 标准笔记，并接入错题库和复习路线。

## 目录

- `AI学习流水线.md`：从 AI 对话导入到复习路线的总入口。
- `对话导入清单.md`：检查待整理材料是否已经进入标准笔记。
- `AI笔记转化看板.md`：检查标准笔记是否要补题号、转错题或拆方法卡。
- `01_待整理/00_AI对话导入入口`：把每节导出的 AI 对话放这里。
- `01_待整理/01_普通笔记草稿`：放课堂摘记、草稿总结。
- `01_待整理/02_题解复盘`：放一题或一组题的复盘。
- `02_标准笔记`：DeepSeek/Claude Code 整理后的标准笔记会放这里。
- `03_原始归档`：以后如果要归档原始材料，可以放这里。
- `04_运行记录`：生成的提示词、API 运行日志会放这里。
- `90_模板`：标准笔记模板和 Claude Code 工作说明。

## 推荐用法

最省事的方式是在总目录直接处理指定文件：

```powershell
.\tools\process_ai_material.ps1 "C:\path\to\一节课AI对话.md"
```

有 `DEEPSEEK_API_KEY` 或 `ANTHROPIC_AUTH_TOKEN` 时会直连整理；没有密钥时会自动生成 DeepSeek 提示词。

## 手动用法

1. 把每节导出的 AI 对话放入 `01_待整理/00_AI对话导入入口`。
2. 先刷新导入清单：

```powershell
python tools/ai_note_manager.py intake
```

3. 如果 DeepSeek v4 Pro 接在 Claude Code 里，先生成提示词：

```powershell
python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口
```

4. 在 Claude Code 中打开生成的 prompt，让它按要求写入 `02_标准笔记`。每批提示词会附带 `prompt_manifest.json`。
5. 整理完成后刷新索引：

```powershell
python tools/ai_note_manager.py index
```

6. 回到总目录运行 `.\tools\maintain_study_systems.ps1`，让新笔记进入错题关联、相似题推荐和今日学习路线。

如果本机环境变量里有 `ANTHROPIC_AUTH_TOKEN` 或 `DEEPSEEK_API_KEY`，也可以直接运行：

```powershell
python tools/ai_note_manager.py run --source 08_AI笔记管理/01_待整理/00_AI对话导入入口 --limit 3
```

直连时脚本默认走 DeepSeek OpenAI 兼容接口，并使用 `DEEPSEEK_API_KEY`。如果只设置了 `ANTHROPIC_AUTH_TOKEN`，脚本也会自动兜底使用它。

数学笔记整理默认开启最高档推理：`DEEPSEEK_THINKING=enabled`、`DEEPSEEK_REASONING_EFFORT=max`。如果临时想省 token，可以把 `DEEPSEEK_THINKING` 设为 `disabled`。

`prompts` 默认跳过已整理过的原始文件；需要强制重做时加 `--force`。
