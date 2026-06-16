# 工具

## 刷新看板

推荐运行：

```powershell
.\tools\update_wrong_bank.ps1
```

也可以直接运行：

```powershell
python tools/refresh_wrong_bank.py
```

作用：

- 扫描 `01_错题` 下所有 `type: "wrong_problem"` 的 Markdown。
- 更新 `00_控制台/错题看板.html`。
- 更新 `00_控制台/错题统计.md`。
- 更新 `00_控制台/系统体检.md`。
- 更新 `00_控制台/复习日历.md`。

建议每次批量导入或修改复习状态后运行一次。
