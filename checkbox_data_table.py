import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkbox_data(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=180)
    # Crea un nuevo contexto de navegador con un tamaño de ventana específico
    #  configurado para grabar video
    context=browser.new_context(
        viewport={'width':1500, 'height':800},
        record_video_dir="videos/checkbox"
    )
    #Se crea el context
    page = context.new_page()
    #Set del timeout para fallas a 4seg  en vez de 30
    page.set_default_timeout(4000)
    #Visitar la web de practica automation
    page.goto("https://datatables.net/extensions/select/examples/checkbox/checkbox.html")
    # Validación del titulo del site
    expect(page).to_have_title("DataTables example - No ordering")
    #time.sleep(1)
    #Hace scroll a 400 px de la coordenada 'y'
    page.mouse.wheel(0,400)
    # Selecciona uno por uno
    for i in range(2,12):
        page.locator(f"(//input[contains(@type,'checkbox')])[{i}]").check()
        #time.sleep(0.5)
    # Selecciona cada 3 
    for i in range(2,12,2):
        page.locator(f"(//input[contains(@type,'checkbox')])[{i}]").check()
        #time.sleep(0.5)
    # Cada 3 seleccionados cambia la pagina
    for i in range(2,12):
        page.locator(f"(//input[contains(@type,'checkbox')])[{i}]").click()
        #time.sleep(0.5)
        if i == 4:
            page.locator("//button[@class='dt-paging-button'][contains(.,'2')]").click()
        if i == 7:
            page.locator("//button[@class='dt-paging-button'][contains(.,'3')]").click()
        if i == 9:
            page.locator("//button[@class='dt-paging-button'][contains(.,'4')]").click()
    # Recorre 4 paginas
    for i in range(2,12):
        page.locator(f"(//input[contains(@type,'checkbox')])[{i}]").check()
        if i==11:
            page.locator("//button[@class='dt-paging-button'][contains(.,'2')]").click()
            for x in range(2,12):
                page.locator(f"(//input[contains(@type,'checkbox')])[{x}]").check()
                if x == 11:
                    page.locator("//button[@class='dt-paging-button'][contains(.,'3')]").click()
                    for y in range(2,12):
                        page.locator(f"(//input[contains(@type,'checkbox')])[{y}]").check()
                        if y == 11:
                            page.locator("//button[@class='dt-paging-button'][contains(.,'4')]").click()
                            for q in range(2,12):
                                page.locator(f"(//input[contains(@type,'checkbox')])[{q}]").check()
    # Recorre las páginas y selecciona los checkboxes con optimización
    for page_num in range(2, 6):
        for i in range(2, 12):
            page.locator(f"(//input[contains(@type,'checkbox')])[{i}]").check()
        if page_num < 5:
            page.locator(f"//button[@class='dt-paging-button'][contains(.,'{page_num}')]").click()

    page.locator("//input[contains(@type,'search')]").fill("London")
    page.locator("(//input[@class='dt-select-checkbox'])[4]").click()
    page.wait_for_timeout(1000)

    context.close()
    browser.close()