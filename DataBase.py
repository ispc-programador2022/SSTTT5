import pyodbc
import config as cfg

class BaseDatos:

    def __init__(self):
        self.__name = cfg.nameDB
        self.__server = cfg.server
        self.__driver = cfg.driver
        self.__conexion = None
        self.__datos = None

    def conectar(self):
        self.__conexion = pyodbc.connect("DRIVER={" + self.__driver + "};"
                                        "Server=" + self.__server + ";"
                                        "DATABASE=" + self.__name + ";"
                                                                                                                              "Trusted_Connection=yes;")

    def cursor(self):
        # Obtener Cursor
        self.__cursor = self.__conexion.cursor()

    def commit(self, query):
        # Enviar Commit
        esselect = query.count('SELECT')
        if esselect == 0:
            self.__conexion.commit()

    def cerrar(self):
        # Cerrar conexion
        self.__conexion.close()

    def obtener_datos(self, query):
        esselect = query.count('SELECT')
        if esselect > 0:
            self.__datos = self.__cursor.fetchall()

    
    def consulta(self, q, v=None):
        if v:
            self.__cursor.execute(q, v)
        else:
            self.__cursor.execute(q)

    
    def ejecutar(self, query, values=None):
        self.conectar()
        self.cursor()
        self.consulta(query, values)
        self.commit(query)
        self.obtener_datos(query)
        self.cerrar()

        return self.__datos


"""
#Prueba conexión
prueba = BaseDatos()
try:
	prueba.conectar()
	print('Se conectó')
except Exception as e:
	print('No se pudo conectar')
	print(e)
"""
