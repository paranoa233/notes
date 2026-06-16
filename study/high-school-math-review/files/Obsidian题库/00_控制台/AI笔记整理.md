# AI 笔记整理

把零散 md 对话、草稿笔记、题解复盘整理成统一格式笔记的入口。

## 快捷入口

- [[08_AI笔记管理/AI学习流水线|AI学习流水线]]
- [[08_AI笔记管理/对话导入清单|对话导入清单]]
- [[08_AI笔记管理/AI笔记转化看板|AI笔记转化看板]]
- [[08_AI笔记管理/01_待整理/00_AI对话导入入口/README|AI对话导入入口]]
- [[08_AI笔记管理/01_待整理/README|待整理入口]]
- [[08_AI笔记管理/标准笔记索引|标准笔记索引]]
- [[08_AI笔记管理/系统体检|系统体检]]
- [[08_AI笔记管理/90_模板/AI对话整理要求|AI对话整理要求]]
- [[08_AI笔记管理/90_模板/标准笔记模板|标准笔记模板]]
- [[08_AI笔记管理/90_模板/ClaudeCode_DeepSeek整理Prompt|Claude Code 整理说明]]

## 使用步骤

1. 把每节导出的 AI 对话 `.md` 或 `.txt` 放进 `08_AI笔记管理/01_待整理/00_AI对话导入入口`。
2. 刷新导入清单：

```powershell
python tools/ai_note_manager.py intake
```

3. 生成给 Claude Code / DeepSeek v4 Pro 的提示词：

```powershell
python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口
```

4. 在 Claude Code 中使用生成的 prompt，或直接让 Claude Code 按整理说明处理待整理目录。
5. 整理完成后刷新索引：

```powershell
python tools/ai_note_manager.py index
```

## 如果要直接调用 API

本机环境变量里有 `ANTHROPIC_AUTH_TOKEN` 或 `DEEPSEEK_API_KEY` 时，可以直接跑：

```powershell
python tools/ai_note_manager.py run --limit 3
```

先小批量跑 `--limit 3`，确认格式满意后再扩大数量。

脚本默认使用 DeepSeek OpenAI 兼容接口：

- `DEEPSEEK_API_KEY`：API 密钥。
- `DEEPSEEK_MODEL`：模型名，默认 `deepseek-v4-pro`。
- `DEEPSEEK_OPENAI_API_URL`：默认 `https://api.deepseek.com/v1/chat/completions`。
- `DEEPSEEK_THINKING`：默认 `enabled`。
- `DEEPSEEK_REASONING_EFFORT`：默认 `max`，用于数学整理时尽量多推理和自检。

如果你更想走 Anthropic 兼容接口，可以临时设置：

```powershell
$env:DEEPSEEK_API_STYLE = "anthropic"
```

如果只是想省 token，可以临时关闭 thinking：

```powershell
$env:DEEPSEEK_THINKING = "disabled"
```
