import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#comando exe pytest --slowmo 750 --headed input2.py
#FUNCION PRINCIPAL DEL TEST
    #==============================================================================================
    # SE PROBARA LOS CHECKBOX CON MUNU DESPLEGABLE MULTIPLE OPCION 2/3
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

    # opción 1
    page.locator("[aria-label=Toggle]").click()
    # opción 2
    page.locator("[aria-label=Toggle]").nth(1).click()
    # opción 3
    #page.locator("text=Commands").click()
    # Cierra el contexto del navegador y el navegador
    
    page.locator("text=NotesCommands >> svg").nth(2).click()

    # Cierra el contexto del navegador y el navegador
    context.close()
    browser.close()