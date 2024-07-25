import re
from playwright.sync_api import Page, expect

def test_uno(page: Page):
    # visitar sitio
    page.goto("https://playwright.dev/")
    #validar si el titulo contiene el texto "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))
    #selector del boton
    buton_uno=page.locator("text=Get started")
    #validacion del href
    expect(buton_uno).to_have_attribute("href","/docs/intro")
    # tomar foto
    page.screenshot(path="capturas/test_uno.png")
    # hacer click en get estarted
    buton_uno.click()
    #validar si hizo click
    page.screenshot(path="capturas/test_uno_click.png")
    # validar endpoint relativo de documentacion
    expect(page).to_have_url(re.compile(".*/docs/intro"))
