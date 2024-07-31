from playwright.sync_api import Page, expect, sync_playwright, Playwright
from funciones import Global_functions

def test_select_1(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=250)
    context = browser.new_context(
        viewport={"width": 1600, "height": 800},
        #record_video_dir='videos/select'
    )
    page=context.new_page()
    page.goto('https://demoqa.com/select-menu')

    page.set_default_timeout(5000)
    #page.mouse.wheel(0,500)
    #time.sleep(1)
    # Crear objeto función global
    gf=Global_functions(page)
    # Utilizar las funciones creadas
    gf.scroll_xy(0,600,2000) #Hace scroll a 400 pixeles de la coordenada x
    gf.wait_s(3000)#Remplazo de time.sleep por wait_timeout



    context.close()
    browser.close()