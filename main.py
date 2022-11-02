from scraping import Inflacion, Ventas

class Menu:

    @staticmethod
    def inicio():
        print("========== Bienvenido ===========")
        print("1 - Obtener información - Scraping")
        print("2 - Ej. Procesamiento de datos - Estadística")
        print("3 - Ej. Graficos etc")

        opcion = int(input("Ingrese la opción y presione enter: "))

        if(opcion == 1):
            Menu.scraping()
        elif(opcion == 2):
            print("EN DESARROLLO...")
            Menu.inicio()
        elif(opcion == 3):
            print("EN DESARROLLO...")
            Menu.inicio()

    @staticmethod
    def scraping():
        print("Aguarde un momento, se recopilará la información estática y dinámica...")
        Ventas.scraping()
        print("Se ha guardado el archivo ventas.csv en la raiz del proyecto")
        print("Se abrirá una ventana del navegador para recopilar la información dinámica...")
        Inflacion().get_data()
        print("Se ha guardo con éxito el archivo inflación.csv... volviendo al menu principal")
        Menu.inicio()

Menu.inicio()