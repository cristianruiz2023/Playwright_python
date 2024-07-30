#playwright codegen https://demoqa.com/checkbox

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    # Crea un nuevo contexto de navegador con un tamaño de ventana específico
    #  configurado para grabar video
    context=browser.new_context(
        viewport={'width':1500, 'height':800},
        #record_video_dir="videos/checkbox"
    )
    page = context.new_page()
    page.goto("https://demoqa.com/checkbox")
    page.get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^Desktop$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Commands").get_by_role("img").first.click()
    page.locator("li").filter(has_text=re.compile(r"^Documents$")).get_by_label("Toggle").click()
    page.locator("li").filter(has_text=re.compile(r"^WorkSpace$")).get_by_label("Toggle").click()
    page.locator("label").filter(has_text="Angular").get_by_role("img").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
