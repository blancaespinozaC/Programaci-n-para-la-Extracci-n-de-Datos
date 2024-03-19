import pandas as pd
"""Escribir un programa que genere y muestre por pantalla un DataFrame con los datos
de la tabla siguiente:"""

def Tabla_dataframe(datos:dict):
    df=pd.DataFrame(datos)
    return df

if __name__ == "__main__":
    datos = {
        "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
        "Ventas": [30500, 35600, 28300, 33900],
        "Gastos": [22000, 234000, 18100, 20700]
    }

    df=Tabla_dataframe(datos)
    print(df)

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 17/03/2024
# Descripción: Esta es un programa en el cual se hace como una tabla con meses, ventas y gastos
#segun lo que venia en la tabla de tarea, se utilizo la libreria de pandas con pd.


print("///////////////////////////////////////////////////////////////////////////////////////////////////////////")
"""El archivo cotización.csv visto en clase contiene las cotizaciones de las empresas
del IBEX35 con las siguientes columnas: nombre (nombre de la empresa), Final
(precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante
la jornada), Mínimo (precio mínimo de la acción durante la jornada), volumen
(Volumen al cierre de bolsa), Efectivo (capitalización al cierre en miles de euros).
Construir una función que construya un DataFrame a partir del archivo con el
formato anterior y devuelve otro DataFrame con el mínimo, el máximo y la media de
cada columna."""




def creacion_dataset(path, separador=",", decimal=".", miles=None):
    datos = pd.read_csv(path, sep=separador, decimal=decimal, thousands=miles)

    n=datos.select_dtypes(include=["float64", "int64"])

    resumen = {
            'Mínimo': n.min(),
            'Máximo': n.max(),
            'Media': n.mean()
        }
    dataframe2=pd.DataFrame(resumen)


    return datos,dataframe2


if __name__ == "__main__":
    df, resumen_df = creacion_dataset("datasets/cotizacion.csv", ";", ",", ".")
    print("DataFrame1 :")
    print(df)
    print("\nDataFrame2:")
    print(resumen_df)
# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 18/03/2024
# Descripción: En este dataframe se utiliza la libreria de pandas en el cual con el archivo de cotizacion.csv
#sacamos un resumen donde viene la maxima, la minima y la media del dataframe, para la realicion reutlice los datos
#del trabajo realizado en la clase como guia.
print("///////////////////////////////////////////////////////////////////////////////////////////////////////////")

"""El archivo titanic.csv visto en clase contiene información sobre los pasajeros del
Titanic. Escribir un programa con los siguientes requisitos:
a. Generar un DataFrame con los datos del archivo.
b. Mostrar el número de datos que contiene y los nombres de sus columnas.
c. Mostrar las 10 primeras filas.
d. Mostrar las 10 últimas filas.
e. Mostrar 10 filas de manera aleatoria."""



def mostrar_informacion_titanic():
    df = pd.read_csv("datasets/titanic.csv")

    print(df)
    print("-----------------------------------------------")
    print("Número de datos en el DataFrame:", df.shape[0])
    print("Número de columnas:", df.shape[1])
    print("Nombres de las columnas:", df.columns.tolist())

    print("-----------------------------------------------")
    print("\nPrimeras 10 filas:")
    print(df.head(10))

    print("-----------------------------------------------")
    print("\nÚltimas 10 filas:")
    print(df.tail(10))

    print("-----------------------------------------------")
    print("\n10 filas de manera aleatoria:")
    print(df.sample(10))

if __name__ == "__main__":
    mostrar_informacion_titanic()

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 18/03/2024
# Descripción: En este dataframe se utiliza la libreria de pandas en el cual con el archivo de titanic.csv en el cual
# saque los  numero de datos del archivo, el numero de columnas, los nombres de la columna, como tambien
# las 10 primeras filas, las 10 ultimas filas y 10 filas al azar.  