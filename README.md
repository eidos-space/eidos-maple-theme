# Maple Mono theme

Maple Mono is a standalone **Eidos Lite host theme plugin**. It applies the [Maple Mono](https://github.com/subframe7536/maple-font) typeface to the Lite interface, editor, and code surfaces, with warm maple light and dark palettes. Theme selection is global to this Lite installation; this is not a style for one plugin view.

The small [`plugin.json`](plugin.json) points to [`theme.css`](theme.css), which defines the two appearances and local `@font-face` rules. The installable package contains validated CSS and two embedded WOFF2 fonts. It has no JavaScript, remote font request, network permission, or Space data access. The regular and bold faces cover the original font's 1,435 glyphs. The upstream WOFF2 has no CJK ideographs, so Chinese text uses the system CJK fallback in `theme.css`.

## Install

Requires an Eidos Lite build with **Plugin API 1.6.0**. In Lite, choose **Plugins → Install plugin…** and select `dist/eidos.maple-theme-0.1.0.eidos-plugin`, or drop the archive into Plugin Manager. Open **Maple Mono** and choose **Apply theme**. Lite's appearance setting selects the matching light or dark palette. **Use default theme** restores the built-in theme.

## Check and package

Point the scripts at an Eidos source checkout containing Plugin API 1.6.0 tooling. No npm dependency install is needed.

```sh
export EIDOS_REPO_DIR=/absolute/path/to/eidos
cd eidos-maple-theme
npm run check
npm run pack:plugin
```

The output is a `.eidos-plugin` file and adjacent SHA-256 file in `dist/`. CLI Serve cannot run Lite themes; the CLI can check and package them.

## Font source and license

The source is the upstream [v7 WOFF2 variable font](https://github.com/subframe7536/maple-font/blob/c08fda97fef73d68c1755219852150770f6e6578/woff2/var/MapleMono%5Bwght%5D-VF.woff2) at commit `c08fda97fef73d68c1755219852150770f6e6578` (SHA-256 `e7080ef37fa8b3a38f71446e53e546634c27ce2cfe97673478cafc029d6344ee`). The bundled regular and bold files are static instances at weights 400 and 700, generated with `scripts/build-fonts.py`. Their family name is **Eidos Maple Mono** to identify the modification. Each bundled font embeds the complete upstream [SIL Open Font License 1.1](OFL.txt) and copyright notice in its name metadata; the same license is included here as `OFL.txt`.

To regenerate the static faces, install `fonttools` and `brotli` for Python, then run:

```sh
python scripts/build-fonts.py
```
