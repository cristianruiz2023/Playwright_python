import re
import time
from playwright.sync_api import Page, expect, Playwright, sync_playwright

#comando exe pytest --slowmo 750 --headed input2.py
#FUNCIÓN PRINCIPAL DEL TEST
    #==============================================================================================
    # SE PROBARA LOS CUADROS DE TEXTO 
    #==============================================================================================
#def test_input2(page: Page):
def test_input2(playwright: Playwright) -> None:
    # Inicia el navegador Chromium en modo no headless (mostrando la ventana) con un retraso 500ms
    browser=playwright.chromium.launch(headless=False, slow_mo=500)
    # Crea un nuevo contexto de navegador con un tamaño de ventana específico
    #  configurado para grabar video
    context=browser.new_context(
        viewport={'width':1500, 'height':800},
        record_video_dir="videos/input2"
    )
    # Crea una nueva página en el contexto del navegador
    page=context.new_page()
    #page.set_viewport_size({'width':500, 'height':400})

     # Navega a la URL especificada
    page.goto("https://demoqa.com/text-box")
    # valida el titulo de la url
    expect(page).to_have_title("DEMOQA")

    #Tiempo de espera
    page.set_default_timeout(4000)

    # Localiza el campo de entrada de nombre de usuario
    nombre=page.locator("#userName")
    # Verifica que el campo de entrada de nombre de usuario sea visible
    expect(nombre).to_be_visible()
    # Llena el campo de entrada de nombre de usuario con "Cristian Ruiz"
    page.locator("#userName").fill("Cristian Ruiz")
    # Toma una captura de pantalla del campo de entrada de nombre de usuario
    page.screenshot(path="capturas/input2/username.png")
    # Localiza el campo de entrada de correo electrónico
    email=page.locator("//input[contains(@id,'userEmail')]")
    # Verifica que el campo de entrada de correo electrónico esté habilitado
    expect(email).to_be_enabled()
    # Verifica que el campo de entrada de correo electrónico esté vacío
    expect(email).to_be_empty()
    # Verifica que el campo de entrada de correo electrónico tenga el ID 'userEmail'
    expect(email).to_have_id('userEmail')
     # Llena el campo de entrada de correo electrónico con "Cristian@ruiz.com"
    page.locator("//input[contains(@id,'userEmail')]").fill("Cristian@ruiz.com")
    # Toma una captura de pantalla del campo de entrada de correo electrónico
    page.screenshot(path="capturas/input2/useremail.png")
    #tiempo de espera forzado
    #time.sleep(2)#espera 2 segundos
    # Llena el campo de dirección actual
    page.locator('//*[@id="currentAddress"]').fill("address uno")
     # Llena el campo de dirección permanente
    page.locator('#permanentAddress').fill("address dos")

    #validar si submit esta visible
    button=page.locator('//*[@id="submit"]')
    expect(button).to_be_visible()
    # Si el botón está presente, haz clic en él
    if button:
        page.locator('//*[@id="submit"]').click()
    else:
        # Si el botón no se encuentra, imprime un mensaje
        print("No se encontró el botón")
     #Verifica que la URL de la página sea la esperada después del envío
    expect(page).to_have_url("https://demoqa.com/text-box")
    #variable del resumen con su id
    resumen=page.locator("#email")
    #validar el resumen contenga el texto 'Email'
    expect(resumen).to_contain_text("Email:")

    # Cierra el contexto del navegador y el navegador
    context.close()
    browser.close()
    