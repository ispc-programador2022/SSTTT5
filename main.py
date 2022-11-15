# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:22:47 2022

@author: adria
"""

import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm

# ==========================================================================================================================================================
#  CARGA Y REVISION DE DATOS - Analisis preliminar exploratorio
# ==========================================================================================================================================================

#Lectura del enlace  extraido con tenicas de web scrapping
df_ventas = pd.read_csv("ventas.csv", header = 0)


#Resumen dataframes "ventas"
df_ventas.info()

#Top 10  primeras filas
print(df_ventas.head(10))


#Variables/atributos
cols_df_ventas = list(df_ventas.columns)
print(cols_df_ventas)

#Los valores de la columna/atributo "indice_tiempo" son de tipo object, indicando que posiblemente son cadenas de texto
#Convierto dicha columna en serie de tipo datetime64 para trabajar con fechas
#Solo me interesa mes y anio

df_ventas["indice_tiempo"] = pd.to_datetime(df_ventas["indice_tiempo"])
anio_mes = lambda x: x[:7]
df_ventas["fecha"] = df_ventas["indice_tiempo"].astype(str).map(anio_mes)
df_ventas.head(10)


#Verifico los cambios
df_ventas.info()

#Primera Visualizacion Serie de Tiempo de Ventas

#Grafico 1; Evolucion de las Ventas

grafico_uno = plt.plot(df_ventas["indice_tiempo"],df_ventas["ventas_precios_constantes"],label="Vtas. en Supermercados",c="red")

plt.style.use("dark_background")
plt.grid(b=True,lw=0.5)
plt.legend()
plt.title("EVOLUCION DE LAS VENTAS EN SUPERMERCADOS A PRECIOS CONSTANTES", c="red")
plt.xlabel("Anio",c="red")
plt.ylabel("Ventas",c="red")

plt.show()


#Se observa Que es una Serie de Tiempo con Estacionalidad

#Aplicando el filtro Hodrick-Prescott para separar en tendencia y componente ciclico


df_ventas_ciclo, df_ventas_tend = sm.tsa.filters.hpfilter(df_ventas['ventas_precios_constantes'])
df_ventas['tendencia'] = df_ventas_tend

#Grafico 2, Visualizacion  componente tendencia y  componente ciclico.

grafico_dos = df_ventas[["indice_tiempo","ventas_precios_constantes","tendencia"]].plot(x="indice_tiempo")
legend = plt.legend()
legend.prop.set_size(14)
plt.xlabel("Anio",c="black")
plt.ylabel("Ventas",c="black")


# ==========================================================================================================================================================
# VENTAS AÑO 2022
# ==========================================================================================================================================================

#Filtro el anio de interes

df_ventas_2022 = df_ventas.tail(8)
df_ventas_2022.describe()

ventas_mensuales_2022= df_ventas_2022[["fecha","ventas_precios_constantes"]]

#Grafico 3, Ventas Mensuales 2022

grafico_tres = plt.plot(ventas_mensuales_2022["fecha"],ventas_mensuales_2022["ventas_precios_constantes"], label ="Consumo en Supermercados Anio 2022")

plt.style.use("dark_background")
plt.legend()

plt.show()


#Estadisticos Descriptivos

promedio_ventas_2022 = ventas_mensuales_2022["ventas_precios_constantes"].mean()

std_ventas_2022 = ventas_mensuales_2022["ventas_precios_constantes"].std()

median_ventas_2022 = ventas_mensuales_2022["ventas_precios_constantes"].median()

ventas_maximas = ventas_mensuales_2022["ventas_precios_constantes"].max()
mes_ventas_maxima =ventas_mensuales_2022.loc[ventas_mensuales_2022["ventas_precios_constantes"].idxmax(),"fecha"]

ventas_minima = ventas_mensuales_2022["ventas_precios_constantes"].min()
mes_ventas_minima =ventas_mensuales_2022.loc[ventas_mensuales_2022["ventas_precios_constantes"].idxmin(),"fecha"]


#Calculo Variacion Mensual
variacion_mensual = ventas_mensuales_2022["ventas_precios_constantes"]/ventas_mensuales_2022["ventas_precios_constantes"].shift(1) - 1
ventas_mensuales_2022["var_mensual"] = round(variacion_mensual,2)


print(ventas_mensuales_2022)


#Composicion_Ventas Agosto 2022, Ultimo mes de informacion

#Grafico 4, Diagrama de Barras

eje_x_g4 = ['bebidas', 'almacen', 'panaderia', 'lacteos', 'carnes', 'verduleria_fruteria', 'alimentos_preparados_rotiseria', 'articulos_limpieza_perfumeria', 'indumentaria_calzado_textiles_hogar', 'electronicos_articulos_hogar', 'otros']

eje_y_g4 = df_ventas_2022.loc[67,['bebidas', 'almacen', 'panaderia', 'lacteos', 'carnes', 'verduleria_fruteria', 'alimentos_preparados_rotiseria', 'articulos_limpieza_perfumeria', 'indumentaria_calzado_textiles_hogar', 'electronicos_articulos_hogar', 'otros']]

colores = ['#00FFFF','#FFE4C4','#FF7F50','#F0F8FF','#7FFFD4','#FFD700','#FF69B4','#778899','#FFFF00','#000080','#ADFF2F']

grafico_cuatro = plt.barh(eje_x_g4,eje_y_g4, color =colores)

plt.style.use("classic")
plt.title("Composicion del Consumo en Supermercados Agosto 2022")
plt.xlabel("Ventas a precios constantes")
plt.ylabel("Grupo de Articulos")

plt.show()

#Medios De Pago Utilizados Agosto 2022, Ultimo mes de Informacion

df_medios_de_pago = df_ventas_2022[['ventas_totales_medio_pago', 'efectivo', 'tarjetas_debito', 'tarjetas_credito', 'otros_medios']]

#Grafico 5, Diagrama Circular "Medios de Pago Agosto 2022"

lista_medios_de_pagos = ['efectivo', 'tarjetas_debito', 'tarjetas_credito', 'otros_medios']
valores_medios_de_pago_agosto = df_ventas_2022.loc[67,['efectivo', 'tarjetas_debito', 'tarjetas_credito', 'otros_medios']]

grafico_cinco = plt.pie(valores_medios_de_pago_agosto, labels =lista_medios_de_pagos, autopct="%0.1f %%" )

plt.title("Medios de Pago Agosto 2022")
plt.axis("equal")

plt.show()

# ==========================================================================================================================================================
# INFLACION AÑO 2022
# ==========================================================================================================================================================

df_inflacion = pd.read_csv("inflacion.csv", header = 0)

df_inflacion.info()

inflacion_mensual_2022= df_inflacion.loc[3:10]


