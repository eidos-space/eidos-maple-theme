# Maple Mono 主题

Maple Mono 是可独立安装的 **Eidos Lite 宿主主题插件**。它为 Lite 的界面、编辑器和代码区域使用 [Maple Mono](https://github.com/subframe7536/maple-font) 字体，并提供暖色系的浅色、深色配色。主题在本机全局生效，不是某个插件视图的样式。

简短的 [`plugin.json`](plugin.json) 指向 [`theme.css`](theme.css)，后者定义浅色、深色配色和本地 `@font-face`。安装包只有经过校验的 CSS 和两份内嵌的 WOFF2 字体，没有 JavaScript、远程字体请求、网络权限或 Space 数据访问权限。常规体和粗体保留了上游字体的 1,435 个字形。上游这组 WOFF2 不含汉字，因此中文会使用 `theme.css` 中指定的系统中文字体回退。

## 安装

需要支持 **Plugin API 1.6.0** 的 Eidos Lite。打开 **插件 → 安装插件…**，选择 `dist/eidos.maple-theme-0.1.0.eidos-plugin`，也可以把安装包拖入插件管理器。打开 **Maple Mono**，点击 **应用主题**。Lite 的外观设置仍决定浅色或深色配色。点击 **使用默认主题** 可恢复内置主题。

## 检查与打包

把脚本指向包含 Plugin API 1.6.0 工具的 Eidos 源码目录。无需安装 npm 依赖。

```sh
export EIDOS_REPO_DIR=/absolute/path/to/eidos
cd eidos-maple-theme
npm run check
npm run pack:plugin
```

`dist/` 中会生成 `.eidos-plugin` 安装包及其 SHA-256 校验文件。CLI Serve 不能运行 Lite 主题；CLI 可检查和打包主题。

## 字体来源与授权

源文件是上游提交 `c08fda97fef73d68c1755219852150770f6e6578` 中的 [v7 WOFF2 可变字体](https://github.com/subframe7536/maple-font/blob/c08fda97fef73d68c1755219852150770f6e6578/woff2/var/MapleMono%5Bwght%5D-VF.woff2)，SHA-256 为 `e7080ef37fa8b3a38f71446e53e546634c27ce2cfe97673478cafc029d6344ee`。`scripts/build-fonts.py` 从中生成字重 400 和 700 的静态字形。字体家族改名为 **Eidos Maple Mono**，以标识这一修改。打包的两份字体都在名称元数据中内嵌了完整的 [SIL Open Font License 1.1](OFL.txt) 和版权声明；项目目录也保留了 `OFL.txt`。

如需重新生成字体，安装 Python 的 `fonttools` 和 `brotli` 后运行：

```sh
python scripts/build-fonts.py
```
