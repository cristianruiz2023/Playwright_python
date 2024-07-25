import re
from playwright.sync_api import Page, expect
#pytest --slowmo 1000 --headed test_dos.py

def test_dos(page: Page):
    # visitar sitio
    page.goto("https://demoqa.com/")
    expect(page).to_have_title("DEMOQA")

    #button hamburger
    page.locator('text=Elements').click()
    page.screenshot(path='capturas/test_dos_button_hamb.png')
    #validar end point
    expect(page).to_have_url(re.compile(".*elements"))

    # button text box

    page.locator('text=Text Box').click()
    page.screenshot(path='capturas/test_dos_button_text_box.png')
    # validar endpoint relativo del form
    expect(page).to_have_url(re.compile(".*/text-box"))

    # text box full name

    page.locator('#userName').fill('cristian ruiz')
    page.screenshot(path='capturas/test_dos_text_box_full_name.png')

    # text box email

    page.locator('#userEmail').fill('cristian@ruiz.com')
    page.screenshot(path='capturas/test_dos_text_box_email.png')

    #current adreess
    page.locator("//TEXTAREA[@id='currentAddress']").fill('adreess uno')
    page.screenshot(path='capturas/test_dos_text_box_curadreess.png')
    #permanent adreess
    page.locator('#permanentAddress').fill('adreess dos')
    page.screenshot(path='capturas/test_dos_text_box_permadress.png')
    #button submit
    page.locator('#submit').click()
    page.screenshot(path='capturas/test_dos_button_submit.png')
    expect(page).to_have_url(re.compile(".*/text-box"))

    