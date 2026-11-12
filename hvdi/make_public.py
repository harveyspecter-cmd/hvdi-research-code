# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
# Contact: bpgp25sushant@iima.ac.in
#
# PROPRIETARY AND CONFIDENTIAL: Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
"""Write the public copy of the page: same page, header notice reduced to one line."""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT.parent / "site-public"
NOTICE = "<!-- Confidential Research © -->"


def main() -> None:
    html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    html, n = re.subn(r"<!--.*?All Rights Reserved.*?-->", NOTICE, html, count=1, flags=re.S)
    if n != 1 or "@" in html.split("</head>")[0].split("<style")[0]:
        raise SystemExit("header notice not replaced cleanly")
    footer = "Beyond the Hype Cycle. Sushant Gaurav, IIMA BPGP 2025-27 Live Project."
    if html.count(footer) != 1:
        raise SystemExit("footer line not found exactly once")
    html = html.replace(footer, "Confidential Research \u00a9")
    OUT.mkdir(exist_ok=True)
    for old in OUT.iterdir():
        old.unlink()
    (OUT / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()
