# Agent导入与分析说明

本文件给 agent 使用。目标是把用户上传的错题材料整理成结构化 Markdown，并保持和原题库分类一致。

## 目录规则

- 错题正文放入 `01_错题/大类/小节`。
- 无法判断分类时，先放入 `01_错题/00_待分类`。
- 图片放入 `05_附件/images`，PDF、Word 等原件放入 `05_附件/docs`。
- 原始待处理材料放在 `99_导入入口`，导入完成后不要删除，除非用户明确要求。

## 分类规则

优先按以下顺序判断分类：

1. 用户给出的原题号或讲义编号，例如 `10-3-3` 属于 `10_数列/10-3_特征根`。
2. 题目来源文件名，例如 `4-6导数选填：构造函数` 属于 `4_导数选填/4-6_构造函数`。
3. 题目知识点和解法关键词。
4. 仍不确定时，写入 `00_待分类`，并在 YAML 的 `classification_confidence` 写 `low`。

分类以 `00_控制台/分类清单.csv` 为准。不要自行新增大类；确需新增时先放入 `00_待分类`。

## 单题文件要求

每道错题必须是一份独立 Markdown，使用 `90_模板/错题模板.md` 的字段和标题。必须保留 YAML 头，至少填写：

- `type: "wrong_problem"`
- `wrong_id`
- `lesson_id`
- `module_id`
- `module`
- `topic`
- `status`
- `priority`
- `wrong_reason`
- `knowledge_points`
- `methods`
- `anti_mistake_tip`
- `created`

如果信息缺失，填 `待补充`，不要编造。公式保留为 LaTeX，行内公式用 `\( ... \)`，展示公式用 `$$ ... $$`。

## 字段规范

- `priority`：`P1`、`P2`、`P3`。P1 表示马上要修的高频或严重错题；P2 表示常规错题；P3 表示低频或已经接近掌握。
- `mastery`：1 到 5，数字越高越稳。
- `review_stage`：`new`、`reviewing`、`stable`、`archived`。
- `next_review`：建议首次导入后填明天或 3 天内；无法判断时留空。
- `anti_mistake_tip`：一句话写“下次看到什么信号就该怎么做”，不要写空泛鸡汤。
- `quality_flags`：记录 `题干待确认`、`答案待确认`、`分类待确认`、`OCR待校对` 等。

## 导入步骤

1. 读取 `99_导入入口` 中的新材料。
2. OCR 或解析题目、我的错误答案、正确答案、解析、来源。
3. 按分类规则确定 `module`、`topic`、`lesson_id`。
4. 按模板生成 Markdown。
5. 文件名优先用 `原题号_错题.md`；无原题号时用 `小节编号-W序号.md`。
6. 将文件放入对应小节目录。
7. 在错题页中链接原始附件和相关原题库题号。
8. 给出 `priority`、`mastery`、`next_review` 的初始建议。
9. 导入结束后运行或提示用户运行 `tools/update_wrong_bank.ps1`，刷新统计、看板、系统体检和复习日历。

## 分析规则

分析错题时，只统计 `type: "wrong_problem"` 的 Markdown。重点读取 YAML 和以下小节：

- `## 错因定位`
- `## 正确解法`
- `## 防错提醒`
- `## 重练记录`

建议输出：

- 按专题、小节统计错题数量。
- 按 `wrong_reason` 找高频问题。
- 找 `status` 为 `待复习` 或 `仍错` 的题。
- 找 `next_review` 早于或等于今天的题。
- 对 `mastery <= 2` 或 `repeat_count >= 2` 的题给出优先级。
- 对 `quality_flags` 不为空或 `classification_confidence = low` 的题列入质量检查。

## 不要做的事

- 不要改动 `Obsidian题库` 原题库。
- 不要把多道错题塞进同一个 Markdown。
- 不要为了整齐而删掉原始题干、用户错误过程或图片证据。
- 不要把猜测写成确定结论；不确定就标注 `待确认`。
