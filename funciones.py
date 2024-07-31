from playwright.sync_api import Page, expect, sync_playwright, Playwright

class Global_functions:
    # Constructor: se ejecuta cuando se crea una instancia de la clase
    def __init__(self,page):
        # Asigna el objeto `page` pasado como argumento a la variable de instancia `self.page`
        self.page = page 

    # Método para esperar un número específico de milisegundos
    def wait_s(self,milliseconds=500):# arg default 500 milisegundos
        # Usa el método `wait_for_timeout` de Playwright para esperar `milliseconds`
        self.page.wait_for_timeout(milliseconds)

    # Método para desplazar (scroll) la página en la dirección x e y y luego esperar
    def scroll_xy(self,x,y,milliseconds=500):# arg default 500 milisegundos
        # Usa el método `wheel` del objeto `mouse` para desplazar la página en x e y
        self.page.mouse.wheel(x,y)
        # Espera `milliseconds` después de desplazar para continuar con la siguiente orden
        self.page.wait_for_timeout(milliseconds)