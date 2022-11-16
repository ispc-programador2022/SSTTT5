from scraping import Inflacion, Ventas
from DataSql import *
class Menu:

    @staticmethod
    def inicio():
        print("========== Bienvenido ===========")
        print("1 - Obtener información - Scraping")
        print("2 - Ver o cargar los datos a la base de datos")
        print("3 - Ej. Procesamiento de datos - Estadística")
        print("4 - Ej. Graficos etc")


        opcion = int(input("Ingrese la opción y presione enter: "))

        if(opcion == 1):
            Menu.scraping()
        elif(opcion == 2):
            Menu.data_sql()
        elif(opcion == 3):
            print("EN DESARROLLO...")
            Menu.inicio()

    @staticmethod
    def scraping():
        print("Aguarde un momento, se recopilará la información estática y dinámica...")
        Ventas.scraping()
        print("Se ha guardado el archivo ventas.csv en la raiz del proyecto")
        print("Se abrirá una ventana del navegador para recopilar la información dinámica...")
        Inflacion()
        print("Se ha guardo con éxito el archivo inflación.csv... volviendo al menu principal")
        Menu.inicio()
    @staticmethod
    def data_sql():
        print("1 - Cargar los datos del scraping a la base de datos")
        print("2 - Ver los datos existentes en la base de datos\n")
        print("0 - Volver al menu principal...")
        opcion = int(input("Ingrese la opción y presione enter: "))
        if (opcion == 1):
            print("Cargando los datos de inflación....")
            InflacionSQL().csv_to_sql()
            print("Cargando los datos de ventas....")
            VentasSQL().csv_to_sql()
            Menu.data_sql()
        elif (opcion == 2):
            print("Datos existentes de inflación:\n")
            data = InflacionSQL().getData()
            for d in data:
                print(d)
            print("Datos existentes de ventas:\n")
            data = InflacionSQL().getData()
            for d in data:
                print(d)
            Menu.inicio()
        else:
            Menu.inicio()

Menu.inicio()