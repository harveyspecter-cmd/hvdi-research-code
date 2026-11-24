# Copyright (c) 2026 Sushant Gaurav (BPGP 2025-27, IIMA). All Rights Reserved.
#
# PROPRIETARY (ALL RIGHTS RESERVED): Unauthorized copying, modification, distribution,
# reverse engineering, or use of this file, via any medium, is strictly prohibited
# without the express prior written permission of Sushant Gaurav.
import pathlib

SITE = (pathlib.Path(__file__).resolve().parent / "site" / "index.html").as_uri()
import asyncio, sys
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width": 1280, "height": 900})
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        await pg.goto(SITE)
        await pg.wait_for_timeout(2200)
        await pg.screenshot(path="s1.png")
        await pg.screenshot(path="full.png", full_page=True)
        # interactions
        await pg.click("#sseg button:nth-child(3)")
        await pg.click("#chips button:nth-child(7)")
        await pg.wait_for_timeout(300)
        await pg.screenshot(path="s2.png")
        t = await pg.inner_text("#panel")
        print("PANEL:", t.replace("\n", " | ")[:400])
        await pg.click("#bc button:nth-child(3)")
        print("BE:", (await pg.inner_text("#beout")).replace("\n", " | ")[:200])
        mp = await b.new_page(viewport={"width": 390, "height": 844})
        await mp.goto(SITE)
        await mp.wait_for_timeout(1800)
        await mp.screenshot(path="m1.png")
        print(
            "ERRORS:",
            [e for e in errs if "fontshare" not in e and "ERR_" not in e][:5],
            "net-errs:",
            len([e for e in errs if "ERR_" in e]),
        )
        await b.close()


asyncio.run(main())
