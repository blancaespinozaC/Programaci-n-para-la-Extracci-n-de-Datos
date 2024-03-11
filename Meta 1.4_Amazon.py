import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def amazonin(numero_paginas):
    s = Service(ChromeDriverManager().install())
    option = Options()
    option.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=s, options=option)
    navegador.get("https://www.amazon.com.mx/")
    time.sleep(9)

    txtBuscar = navegador.find_element(By.NAME, "field-keywords")
    txtBuscar.send_keys("audifonos")
    time.sleep(3)

    btnCli = navegador.find_element(By.ID, "nav-search-submit-button")
    btnCli.click()

    for i in range(numero_paginas):
        captura = "imagenes_Amazon/pagina_{}.png".format(i + 1)
        navegador.save_screenshot(captura)

        txtsigui = navegador.find_element(By.LINK_TEXT, "Siguiente")
        txtsigui.click()

        time.sleep(5)

    navegador.close()

if __name__ == "__main__":
    numero_paginas = 3
    amazonin(numero_paginas)
    
