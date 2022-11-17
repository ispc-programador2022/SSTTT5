# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:22:47 2022

@author: adria
"""

import pandas as pd
from matplotlib import pyplot as plt
import statsmodels.api as sm
from io import open

def analysis():
    # ==========================================================================================================================================================
    #  CARGA Y REVISION DE DATOS - Analisis preliminar exploratorio
    # ==========================================================================================================================================================

    #Lectura del archivo (tambien se puede usar el enlace  extraido con tecnicas de web scrapping"
    try:
        df_ventas = pd.read_csv("ventas.csv", header=0)
    except:
        print("No se pudo abrir archivo. Testear el error e intentarlo nuevamente")

    # Resumen dataframes "ventas"
    df_ventas.info()

    # Top 10  primeras filas
    print(df_ventas.head(10))

    # Variables/atributos
    cols_df_ventas = list(df_ventas.columns)
    print(cols_df_ventas)

    # Los valores de la columna/atributo "indice_tiempo" son de tipo object, indicando que posiblemente son cadenas de texto
    # Convierto dicha columna en serie de tipo datetime64 para trabajar con fechas
    # Solo me interesa mes y anio

    df_ventas["indice_tiempo"] = pd.to_datetime(df_ventas["indice_tiempo"])
    anio_mes = lambda x: x[:7]
    df_ventas["fecha"] = df_ventas["indice_tiempo"].astype(str).map(anio_mes)
    df_ventas.head(10)

    # Verifico los cambios
    df_ventas.info()

    # Primera Visualizacion Serie de Tiempo de Ventas

    # --------------------------------------
    # Grafico 1; Evolucion de las Ventas ---
    # --------------------------------------

    plt.plot(df_ventas["indice_tiempo"], df_ventas["ventas_precios_constantes"], label="Vtas. en Supermercados",
             c="red")

    plt.style.use("dark_background")
    plt.grid(b=True, lw=0.5)
    plt.legend()
    plt.title("EVOLUCION DE LAS VENTAS EN SUPERMERCADOS A PRECIOS CONSTANTES", c="red")
    plt.xlabel("Anio", c="red")
    plt.ylabel("Ventas", c="red")

    plt.savefig("grafico1.png")
    plt.show()

    # Se observa Que es una Serie de Tiempo con Estacionalidad
    # Aplico el filtro Hodrick-Prescott para separar en tendencia y componente ciclico

    df_ventas_ciclo, df_ventas_tend = sm.tsa.filters.hpfilter(df_ventas['ventas_precios_constantes'])
    df_ventas['tendencia'] = df_ventas_tend

    # ------------------------------------------------------------------------
    # Grafico 2, Visualizacion  componente tendencia y  componente ciclico. --
    # ------------------------------------------------------------------------

    df_ventas[["indice_tiempo", "ventas_precios_constantes", "tendencia"]].plot(x="indice_tiempo")
    legend = plt.legend()
    legend.prop.set_size(14)
    plt.xlabel("Anio", c="black")
    plt.ylabel("Ventas", c="black")

    plt.savefig("grafico2.png")
    plt.show()

    # ==========================================================================================================================================================
    # VENTAS AÑO 2022
    # ==========================================================================================================================================================

    # Filtro el anio de interes

    df_ventas_2022 = df_ventas.loc[60:67]
    df_ventas_2022.describe()

    ventas_mensuales_2022 = df_ventas_2022[["fecha", "ventas_precios_constantes"]]

    # -------------------------------------
    # Grafico 3, Ventas Mensuales 2022 ----
    # -------------------------------------

    ventas_mensuales_2022[["fecha", "ventas_precios_constantes"]].plot(x="fecha")

    plt.style.use("dark_background")
    plt.title("CONSUMO EN SUPERMERCADOS AGOSTO 2022", c="green")
    plt.xlabel("Anio", c="green")
    plt.ylabel("Ventas", c="green")

    plt.savefig("grafico3.png")
    plt.show()

    # -----------------------------
    # Estadisticos Descriptivos ---
    # -----------------------------

    promedio_ventas_2022 = ventas_mensuales_2022["ventas_precios_constantes"].mean()

    std_ventas_2022 = ventas_mensuales_2022["ventas_precios_constantes"].std()

    median_ventas_2022 = ventas_mensuales_2022["ventas_precios_constantes"].median()

    ventas_maximas = ventas_mensuales_2022["ventas_precios_constantes"].max()
    mes_ventas_maxima = ventas_mensuales_2022.loc[ventas_mensuales_2022["ventas_precios_constantes"].idxmax(), "fecha"]

    ventas_minima = ventas_mensuales_2022["ventas_precios_constantes"].min()
    mes_ventas_minima = ventas_mensuales_2022.loc[ventas_mensuales_2022["ventas_precios_constantes"].idxmin(), "fecha"]

    # Calculo Variacion Mensual
    variacion_mensual = ventas_mensuales_2022["ventas_precios_constantes"] / ventas_mensuales_2022[
        "ventas_precios_constantes"].shift(1) - 1
    ventas_mensuales_2022["var_mensual"] = round(variacion_mensual, 2)

    print(ventas_mensuales_2022)

    # Composicion_Ventas Agosto 2022, Ultimo mes de informacion

    # ---------------------------------
    # Grafico 4, Diagrama de Barras ---
    # ---------------------------------

    eje_x_g4 = ['bebidas', 'almacen', 'panaderia', 'lacteos', 'carnes', 'verduleria_fruteria',
                'alimentos_preparados_rotiseria', 'articulos_limpieza_perfumeria',
                'indumentaria_calzado_textiles_hogar', 'electronicos_articulos_hogar', 'otros']

    eje_y_g4 = df_ventas_2022.loc[67, ['bebidas', 'almacen', 'panaderia', 'lacteos', 'carnes', 'verduleria_fruteria',
                                       'alimentos_preparados_rotiseria', 'articulos_limpieza_perfumeria',
                                       'indumentaria_calzado_textiles_hogar', 'electronicos_articulos_hogar', 'otros']]

    colores = ['#00FFFF', '#FFE4C4', '#FF7F50', '#F0F8FF', '#7FFFD4', '#FFD700', '#FF69B4', '#778899', '#FFFF00',
               '#000080', '#ADFF2F']

    plt.barh(eje_x_g4, eje_y_g4, color=colores)

    plt.style.use("classic")
    plt.title("Composicion del Consumo en Supermercados Agosto 2022")
    plt.xlabel("Ventas a precios constantes")
    plt.ylabel("Grupo de Articulos")

    plt.savefig("grafico4.png")
    plt.show()

    # Medios De Pago Utilizados Agosto 2022, Ultimo mes de Informacion

    df_medios_de_pago = df_ventas_2022[
        ['ventas_totales_medio_pago', 'efectivo', 'tarjetas_debito', 'tarjetas_credito', 'otros_medios']]

    # ------------------------------------------------------------
    # Grafico 5, Diagrama Circular "Medios de Pago Agosto 2022" --
    # ------------------------------------------------------------

    lista_medios_de_pagos = ['Efectivo', 'Tarjetas de Debito', 'Tarjetas de Credito', 'Otros_Medios']
    valores_medios_de_pago_agosto = df_ventas_2022.loc[
        67, ['efectivo', 'tarjetas_debito', 'tarjetas_credito', 'otros_medios']]

    plt.pie(valores_medios_de_pago_agosto, labels=lista_medios_de_pagos, autopct="%0.1f %%")

    plt.title("Medios de Pago Agosto 2022")
    plt.axis("equal")

    plt.savefig("grafico5.png")
    plt.show()

    # ==========================================================================================================================================================
    # INFLACION AÑO 2022
    # ==========================================================================================================================================================

    df_inflacion = pd.read_csv("inflacion.csv", header=0)

    df_inflacion.info()

    inflacion_mensual_2022 = df_inflacion.loc[3:10]

    # ==========================================================================================================================================================
    # RESUMEN DE DATOS -- Persistencia de Datos
    # ==========================================================================================================================================================

    archivo_resumen_datos = open("resumen_estadisticos_descriptivos.txt", "w")

    texto = '''--> Promedio Ventas 2022: 24427.7550 \n \n
    --> Variabilidad Ventas 2022 (Desvío Estándar): 933.0240 \n \n 
    --> Mediana Ventas 2022: 24142.7789 \n \n 
    --> Mes de Mayores Ventas 2022: Julio \n \n 
    --> Monto Total Mayores Ventas 2022: 26090.18031 \n \n 
    --> Mes de Menores Ventas 2022: Mayo \n \n 
    --> Monto Menores Ventas 2022: 23235.0963  \n \n 
    --> Variaciones Mensuales Ventas 2022 \n \n 
    id     fecha  ventas_precios_constantes  var_mensual
    60  2022-01           25464.131520          NaN
    61  2022-02           23803.202023        -0.07
    62  2022-03           24612.901369         0.03
    63  2022-04           24141.199035        -0.02
    64  2022-05           23235.096273        -0.04
    65  2022-06           24144.358859         0.04
    66  2022-07           26090.180313         0.08
    67  2022-08           23930.970811        -0.08'''

    archivo_resumen_datos.write(texto)

    archivo_resumen_datos.close()

