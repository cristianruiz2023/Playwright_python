import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#comando exe pytest --slowmo 750 --headed input2.py
#FUNCIÓN PRINCIPAL DEL TEST
    #==============================================================================================
    # SE PROBARA LOS CHECKBOX CON MENÚ DESPLEGABLE MULTIPLE OPCIÓN 1/3
    #==============================================================================================
#def test_checkbox(page: Page):
def test_checkbox(playwright: Playwright) -> None:
    # Inicia el navegador Chromium en modo no headless (mostrando la ventana) con un retraso 500ms
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    # Crea un nuevo contexto de navegador con un tamaño de ventana específico
    #  configurado para grabar video
    context=browser.new_context(
        viewport={'width':1500, 'height':800},
        #record_video_dir="videos/checkbox"
    )
    # Crea una nueva página en el contexto del navegador
    page=context.new_page()
    page.set_default_timeout(4000)

     # Navega a la URL especificada
    page.goto("https://demoqa.com/checkbox")

    # Opción desplegable 1
    che1 = page.locator("//button[contains(@aria-label,'Toggle')]")
    #time.sleep(1)
    expect(che1).to_be_visible()
    che1.click()
    #time.sleep(1)

    # Opción desplegable 2
    page.locator("(//button[contains(@title,'Toggle')])[2]").click()

    # Opción desplegable 3
    #page.locator("text=Commands").click()
    #time.sleep(1)
    page.locator("//span[@class='rct-title'][contains(.,'Commands')]").click()
    #validación de confirmación de opción seleccionada
    selection = page.locator("//span[contains(.,'You have selected :')]")
    expect(selection).to_contain_text("You have selected")
    
    # Cierra el contexto del navegador y el navegador
    context.close()
    browser.close()