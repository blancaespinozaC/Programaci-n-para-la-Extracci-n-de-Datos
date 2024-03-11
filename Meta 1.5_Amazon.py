import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def extraer_datos_producto():
    s = Service(ChromeDriverManager().install())
    option = Options()
    option.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=s, options=option)
    navegador.get("https://www.amazon.com.mx/")
    time.sleep(9)

    txtBuscar = navegador.find_element(By.NAME, "field-keywords")
    txtBuscar.send_keys("collares mujer")
    btnCli = navegador.find_element(By.ID, "nav-search-submit-button")
    btnCli.click()

    datos = {
        "Nombre": [],
        "Rating": [],
        "Precio": [],
        "Fecha_Entrega": []
    }

    for _ in range(3):  # Cambia el número de páginas según tus necesidades
        time.sleep(3)
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        productos = soup.select("div.s-asin")

        for producto in productos:
            nombre = producto.find("span", class_="a-size-base-plus a-color-base a-text-normal")
            rating = producto.find("span", class_="a-icon-alt")
            precio = producto.find("span", class_="a-price-whole")
            fecha_entrega = producto.find("span", class_="a-text-bold")

            if nombre:
                datos["Nombre"].append(nombre.text.strip())
            else:
                datos["Nombre"].append("Sin nombre")

            if rating:
                datos["Rating"].append(rating.text.strip())
            else:
                datos["Rating"].append("Sin rating")

            if precio:
                datos["Precio"].append(precio.text.strip())
            else:
                datos["Precio"].append("Sin precio")

            if fecha_entrega:
                datos["Fecha_Entrega"].append(fecha_entrega.text.strip())
            else:
                datos["Fecha_Entrega"].append("Sin fecha de entrega")

        siguiente_pagina = navegador.find_element(By.PARTIAL_LINK_TEXT, "Siguiente")
        siguiente_pagina.click()

    df = pd.DataFrame(datos)
    df.to_csv("DataSet/productos_amazon.csv")

    time.sleep(5)
    navegador.close()

if __name__ == "__main__":
    extraer_datos_producto()
