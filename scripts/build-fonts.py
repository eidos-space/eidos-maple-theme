"""Rebuild the two static WOFF2 faces from the pinned upstream variable font.

Requires fonttools and brotli. Generated faces retain the full OFL in their
name-table license field because the Eidos theme archive embeds only fonts.
"""

from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "fonts" / "MapleMono-VF.upstream.woff2"
LICENSE = (ROOT / "OFL.txt").read_text(encoding="utf-8")
FAMILY = "Eidos Maple Mono"


for weight, style in ((400, "Regular"), (700, "Bold")):
    font = TTFont(SOURCE)
    font.flavor = None
    font = instantiateVariableFont(font, {"wght": weight}, inplace=True)
    font.recalcTimestamp = False
    names = font["name"]
    for name_id, value in {
        0: "Copyright 2022 The Maple Mono Project Authors. Modified for Eidos Lite. See license description (name ID 13).",
        1: FAMILY,
        2: style,
        3: f"Eidos Maple Mono {style} 0.1.0",
        4: f"{FAMILY} {style}",
        6: f"EidosMapleMono-{style}",
        13: LICENSE,
        14: "https://openfontlicense.org",
    }.items():
        names.setName(value, name_id, 3, 1, 0x409)
    font.flavor = "woff2"
    output = ROOT / "fonts" / f"EidosMapleMono-{style}.woff2"
    font.save(output)
    print(output)
