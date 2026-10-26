# Maple Mono

A standalone Eidos Lite theme with warm light/dark palettes and bundled [Maple Mono](https://github.com/subframe7536/maple-font) fonts for the interface, editor and code.

Requires **Eidos Lite 0.29.0 or later**, with Plugin API **3.7.0**. Names and documentation follow the app language.

Install from Marketplace or the project's GitHub Release, then choose **Plugins → Maple Mono → Apply theme**. Light, Dark or System selects the palette. The selection applies across Spaces on this device; **Use default theme** clears it.

The archive contains validated CSS and embedded regular/bold WOFF2 fonts, with no executable code, remote fonts, network access or Space data access. The bundled upstream font has 1,435 glyphs and no Chinese glyphs; Chinese uses the configured system-font fallback. CLI Serve, Android and iOS do not support this host theme.

## Development

Use Node.js 22.12 or later and the pinned SDK/tools 0.9.0. Run `npm ci`, `npm run check` and `npm run pack:plugin`. The archive and SHA-256 checksum appear in `dist/`. Upstream font licenses remain bundled with the project.
