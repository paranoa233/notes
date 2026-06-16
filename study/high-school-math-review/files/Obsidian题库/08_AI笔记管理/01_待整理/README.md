# 待整理

这里是所有“还没沉淀成标准笔记”的材料入口。

## 子目录

- [[00_AI对话导入入口/README|00_AI对话导入入口]]：每节 AI 对话导出文件。
- [[01_普通笔记草稿/README|01_普通笔记草稿]]：课堂摘记、草稿总结。
- [[02_题解复盘/README|02_题解复盘]]：一题或一组题的复盘。

## 常用命令

刷新导入清单：

```powershell
python tools/ai_note_manager.py intake
```

为 AI 对话生成 DeepSeek 整理提示词：

```powershell
python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口
```

默认会跳过已经整理过的原始文件。需要重做提示词时：

```powershell
python tools/ai_note_manager.py prompts --source 08_AI笔记管理/01_待整理/00_AI对话导入入口 --force
```

如果希望脚本直接调用 DeepSeek API，可先小批量运行：

```powershell
python tools/ai_note_manager.py run --source 08_AI笔记管理/01_待整理/00_AI对话导入入口 --limit 3
```
