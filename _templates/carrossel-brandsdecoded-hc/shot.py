import asyncio,os
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--allow-file-access-from-files"])
        pg=await b.new_page(viewport={"width":1200,"height":1400})
        await pg.goto("file://"+os.path.abspath("carrossel.html")); await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(500)
        print(await pg.evaluate("[document.fonts.check(\"800 40px 'Barlow Condensed'\"),document.fonts.check(\"500 20px 'Inter'\")]"))
        os.makedirs("out",exist_ok=True)
        for i,el in enumerate(await pg.query_selector_all(".slide, .s")):
            await el.screenshot(path=f"out/{i+1:02d}.png")
        await b.close()
asyncio.run(main())
