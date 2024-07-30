import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_checkbox4(playwright: Playwright) -> None:
    browser=playwright.chromium.launch(headless=False, slow_mo=200)
    # Crea un nuevo contexto de navegador con un tamaño de ventana específico
    #  configurado para grabar video
    context=browser.new_context(
        viewport={'width':1500, 'height':800},
        #record_video_dir="videos/checkbox"
    )
    #Se crea el context
    page = context.new_page()
    #Set del timeout para fallas a 4seg  en vez de 30
    page.set_default_timeout(4000)
    #Visitar la web de practica automation
    page.goto("https://demoqa.com/automation-practice-form")
    #Validación del title del site
    expect(page).to_have_title("DEMOQA")
    #time.sleep(1)
    #Hace scroll a 400 px de la coordenada 'y'
    page.mouse.wheel(0,400)
    #time.sleep(1)
    #Localizar y completar el campo nombre
    page.locator('#firstName').fill('Cristian')
    #time.sleep(1)
    #Localizar y completar el campo apellido
    page.locator('#lastName').fill('Ruiz')
    #Localizar y completar el campo email
    page.locator("//input[@id='userEmail']").fill('Cristain@gmail.com')
    #time.sleep(1)
    #Localizar y completar el campo Number
    page.locator("//input[@id='userNumber']").fill('123456789')

    #Checkbox multiples con .click()
    #time.sleep(1)
    #page.locator("//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]").click()

    #time.sleep(1)
    #page.locator("//label[contains(@for,'hobbies-checkbox-3')]").click()
    #time.sleep(1)
    #page.locator("//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]").click()
    #page.locator("//label[contains(@for,'hobbies-checkbox-3')]").click()

    #Hace scroll a 600 px de la coordenada 'y'
    page.mouse.wheel(0,600) #(X,Y)
    #Checkbox multiples con .check()
    #time.sleep(1)
    #page.locator("//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]").check()

    #time.sleep(1)
    #page.locator("//label[contains(@for,'hobbies-checkbox-3')]").check()
    #assert page.locator("//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]").is_checked() is True

    #time.sleep(1)
    #page.locator("//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]").uncheck()
    #page.locator("//label[contains(@for,'hobbies-checkbox-3')]").uncheck()
    #assert page.locator("//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]").is_checked() is False
    

#"(//label[@class='custom-control-label'])[4]"
    for i in range(4,7):
        #print(i)
        #salida=f"(//label[@class='custom-control-label'])[{i}]"
        #print(salida)
        #page.locator(salida).check()
        page.locator(f"(//label[@class='custom-control-label'])[{i}]").check()
        time.sleep(1)
#(//label[@class='custom-control-label'])[1]
    for i in range(1,4):
        #print(i)
        #salida=f"(//label[@class='custom-control-label'])[{i}]"
        #print(salida)
        #page.locator(salida).check()
        page.locator(f"(//label[@class='custom-control-label'])[{i}]").check()
        time.sleep(1)
    
    context.close()
    browser.close()