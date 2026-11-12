# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
# Contact: bpgp25sushant@iima.ac.in
#
# PROPRIETARY AND CONFIDENTIAL: Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
import pathlib

SITE = (pathlib.Path(__file__).resolve().parent / "site" / "index.html").as_uri()
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=2)
    pg.goto(SITE)
    pg.wait_for_timeout(2200)
    pg.query_selector(".curvebox").screenshot(path="deck_curve.png")
    btns = pg.query_selector_all("#sseg button")
    print([x.inner_text() for x in btns])
    for x in btns:
        if "ndium" in x.inner_text():
            x.click()
    pg.wait_for_timeout(500)
    pg.query_selector("#gates").screenshot(path="deck_gates_indium.png")
    b.close()
