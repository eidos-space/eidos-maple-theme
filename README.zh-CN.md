# Maple Mono 主题

内置 [Maple Mono](https://github.com/subframe7536/maple-font) 字体，为 Eidos Lite 的界面、编辑器和代码区域提供暖色浅色／深色配色。

需要 **Eidos Lite 0.29.0** 及以上版本，支持插件 API **3.7.0**。名称和文档跟随应用语言。

从插件市场或项目的 GitHub Release 安装，选择 **插件 → Maple Mono → 应用主题**。外观设置决定浅色、深色或跟随系统；主题在本机所有 Space 生效，点击 **使用默认主题** 可恢复。

归档只包含经过验证的 CSS 和内嵌的常规／粗体 WOFF2 字体，没有可执行代码、远程字体、网络或 Space 数据访问权限。上游字体包含 1,435 个字形，不包含汉字；中文使用配置的系统字体回退。CLI Serve、Android 和 iOS 不支持此宿主主题。

## 开发

使用 Node.js 22.12 及以上版本及固定的 SDK/tools 0.9.0。依次运行 `npm ci`、`npm run check` 和 `npm run pack:plugin`，归档和 SHA-256 校验文件位于 `dist/`。项目保留上游字体许可。
