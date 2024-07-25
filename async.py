import asyncio
# Importa el módulo handlers de logging, aunque no se utiliza en este código
from logging import handlers
# Importa async_playwright de la API asíncrona de Playwright
from playwright.async_api import async_playwright

async def main():
    """
    Función principal que automatiza el navegador para abrir una página web y 
    obtener el título de la página.
    """
    # Inicia Playwright en un contexto asíncrono
    async with async_playwright() as p:
        # Lanza el navegador Chromium con la interfaz gráfica visible (no en modo headless)
        browser = await p.chromium.launch(headless=False)
        # Crea una nueva página en el navegador
        page = await browser.new_page()
        # Navega a la URL "https://playwright.dev/"
        await page.goto("https://playwright.dev/")
        # Imprime el título de la página
        print(await page.title())
        # Cierra el navegador
        await browser.close()

# Ejecuta la función principal en el bucle de eventos de asyncio
asyncio.run(main())