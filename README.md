# GitHub Pages Markdown 笔记站

这是一个可以直接托管到 GitHub Pages 的静态笔记站模板。

特点：

- 不需要 Node、Ruby 或构建流程
- 直接写 Markdown
- 支持搜索、标签、代码块和数学公式
- 很适合放公开学习笔记、论文记录、备忘卡片

## 目录结构

```text
notes-site/
├─ assets/
│  ├─ app.js
│  └─ style.css
├─ notes/
│  ├─ notes.json
│  └─ *.md
├─ index.html
└─ README.md
```

## 如何新增一篇笔记

1. 在 `notes/` 下面新建一个 Markdown 文件
2. 在 `notes/notes.json` 里增加一条记录
3. 提交并推送到 GitHub

## 如何发布到 GitHub Pages

### 方案一：仓库名随意

1. 在 GitHub 上创建一个新仓库，例如 `notes-site`
2. 把这个目录下的全部文件上传到仓库根目录
3. 打开 GitHub 仓库设置里的 `Pages`
4. 在 `Build and deployment` 里选择 `Deploy from a branch`
5. 分支选 `main`，目录选 `/ (root)`
6. 保存后，GitHub 会给你一个公开地址

地址一般会是：

```text
https://你的用户名.github.io/仓库名/
```

### 方案二：做成个人主页主站

如果你把仓库名建成：

```text
你的用户名.github.io
```

那网站地址就会直接变成：

```text
https://你的用户名.github.io/
```

## 本地预览

如果你想在本地先看效果，可以在这个目录运行：

```powershell
python -m http.server 8000
```

然后浏览器打开：

```text
http://localhost:8000
```

## 维护时最常改的文件

- `index.html`：页面骨架
- `assets/style.css`：样式
- `assets/app.js`：交互逻辑
- `notes/notes.json`：笔记清单
- `notes/*.md`：具体内容

## 以后可继续扩展

如果你想增强“交流”能力，下一步很适合继续加：

- Giscus 评论区
- 自定义域名
- 首页精选笔记
- 按年份或主题归档
- 自动生成 `notes.json` 的小脚本
