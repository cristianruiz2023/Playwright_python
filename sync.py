import asyncio
# Importa el módulo handlers de logging, aunque no se utiliza en este código
from logging import handlers
# Importa sync_playwright de la API síncrona de Playwright
from playwright.sync_api import sync_playwright

# Inicia Playwright en un contexto síncrono
with sync_playwright() as p:
    # Lanza el navegador Chromium con la interfaz gráfica visible (no en modo headless) 
    # y un retraso (slow motion) de 4000 ms entre acciones
    browser = p.chromium.launch(headless=False, slow_mo=4000)
    # Crea una nueva página en el navegador
    page = browser.new_page()
    # Navega a la URL "https://demoqa.com"
    page.goto("https://demoqa.com")
    # Imprime el título de la página
    print(page.title())
    # Cierra el navegador
    browser.close()