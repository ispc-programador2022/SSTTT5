from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
import config as cfg
import requests


class Inflacion:

    def __int__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://es.investing.com/economic-calendar/argentinian-cpi-436")
        self.more_data = WebDriverWait(self.driver, 1).until(EC.visibility_of_all_elements_located((By.ID, "showMoreHistory436")))


    def get_data(self):
        self.__int__()
        self.scraping()


    def onclick(self, clicks):
        for i in range(0, clicks):
            self.more_data[0].click()
            time.sleep(cfg.tiempo_click)


    def scraping(self):
        self.onclick(cfg.cant_clicks)
        page_code = self.driver.page_source
        soup = BeautifulSoup(page_code, 'lxml')
        data = soup.find("table", {"id": "eventHistoryTable436"})
        fechas = data.find_all("td", {"class": "left"})
        datos_inflacion = data.find_all("td", {"class": "noWrap"})
        self.save_csv(fechas, datos_inflacion)
        self.driver.quit()


    def filtrar_fechas(self, fechas):
        datos_ord = list()
        for i in range(0, len(fechas), 2):
            fecha = str(fechas[i])
            datos_ord.append(fecha[17:27])

        return datos_ord


    def filtrar_inflacion(self, inflacion):
        percent = list()
        caracteres = ",1234567890%"

        for i in range(0, len(inflacion), 3):
            palabra = ''
            element = str(inflacion[i])
            for s in element:
                if s in caracteres:
                    palabra += s
            percent.append(palabra)
        return percent


    def save_csv(self, fechas, datos_inflacion):

        fechas = self.filtrar_fechas(fechas)
        inflacion = self.filtrar_inflacion(datos_inflacion)

        datos = {"fecha": fechas, "variacion_mensual": inflacion}
        df = pd.DataFrame(datos, columns=['fecha', 'variacion_mensual'])
        df.to_csv('inflacion.csv', index=False)


class Ventas:

    @staticmethod
    def scraping():
        URL = "https://datos.gob.ar/dataset/sspm-ventas-supermercados"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "lxml")
        data = soup.find("div", {"class": "pkg-actions"})
        info = list()
        for i in data:
            info.append(str(i))
        link = info[3][9:123]
        Ventas.download_csv(link)

    @staticmethod
    def download_csv(url):
        myfile = requests.get(url)
        open('ventas.csv', 'wb').write(myfile.content)




