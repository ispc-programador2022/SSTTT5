from DataBase import BaseDatos
import pandas as pd

class InflacionSQL:

    def __init__(self):
        self.sql = BaseDatos()
        self.tableName = "inflacion"


    def csv_to_sql(self):
        data = self.open_csv()
        query = "INSERT INTO " + self.tableName + "(fecha, porcentaje) VALUES (?,?)"
        errors = 0
        for d in data:
            values = tuple(d)
            try:
                self.sql.ejecutar(query, values)
            except:
                errors += 1
        print(f"Transacción realizada, se han encontrado {errors} conflictos")

    def getData(self):
        query = "SELECT * FROM " + self.tableName
        data = self.sql.ejecutar(query)
        return data

    def open_csv(self):
        data = pd.read_csv('inflacion.csv')
        return data.values[:73]


class VentasSQL:

    def __init__(self):
        self.sql = BaseDatos()
        self.tableName = "ventas"

    def csv_to_sql(self):
        data = self.open_csv()
        name_columns = str(tuple(data.columns.values))
        values = "?," * len(data.columns.values)
        query = "INSERT INTO " + self.tableName + name_columns.replace("'", "") + " VALUES ("+ values[:len(values)-1] +")"
        errors = 0

        for d in data.values:

            try:
                self.sql.ejecutar(query, tuple(d))
            except:
                errors += 1

        print(f"Transacción realizada, se han encontrado {errors} conflictos")

    def getData(self):
        query = "SELECT * FROM " + self.tableName
        data = self.sql.ejecutar(query)
        return data

    def open_csv(self):
        data = pd.read_csv('ventas.csv')
        return data
