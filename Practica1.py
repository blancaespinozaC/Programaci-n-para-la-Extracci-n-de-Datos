"""Ejercicios Listas, Tuplas, Sets y Diccionarios.

Nota: Para todos los
ejercicios, incluir como comentarios su nombre completo, grupo, fecha de realización, y
descripción del problema.

Duplicados.Desarrolle una función que dada una lista de números enteros, retorna True si al menos
un valor aparece dos veces, y Falso si todos los elementos son distintos.

Ejemplos:
nums = [1, 2, 3, 1]
duplicados(nums)
True

nums = [1, 2, 3, 4]
duplicados(nums)
False

RETO: Intentar solucionar problema, solo con una línea de código dentro de la función.Sin contar el llamado
y / o pruebas de las funciones.

Suma de dos números.Dado una lista de números enteros y un valor entero(target), retorna el
índice de los dos números que sumados sean igual al target.Debe asumir  que existe siempre
una única solución, y que un mismo elemento no se puede usar dos veces.Debes retornar una tupla con los índices.

# #
Ejemplos:
nums = [2, 7, 11, 15]
target = 9
busquedaSuma(nums, target)
(0, 1)


nums = [3, 2, 4]
target = 6
busquedaSuma(nums, target)
(1, 2)

RETO: Intentar solucionar problema como máximo usando un ciclo.Puedes usar variables, condiciones
y / o estructuras auxiliares.

Análisis de Población.Tienes datos sobre población de diferentes ciudades representados como
tuplas(ciudad, población, área).Crea funciones para:

a.Calcular la densidad de población(población dividida por la cantidad total de población
por área) para cada ciudad.

#primero sacar la densidad de poblancion y despues dividir#

b.Identificar la ciudad con la mayor densidad de población.

Ejemplo:
ciudades = [(“Tijuana”, 5, “NoroEste”),
            (“Ciudad de Mexico”, 8, “Centro”),
            (“Ensenada”, 3, “NoroEste”),
            (“Puebla”, 3, “Centro”),
            (“Cancun”, 4, “Sur”)
            ]

densidades = calcular_densidades(ciudades)
mayor = mayor_densidad(ciudades)

print(densidades)
# {“Tijuana”: 0.62, “Ciudad de Mexico”: 0.72, “Ensenada”: 0.37, “Puebla”:0.27, “Cancun”: 4}

print(mayor)
# “Ciudad de México”

Estadística Básica.Cree una clase llamada Estadística que contiene como atributo una
lista de números naturales la cual puede contener repetidos.
Debe contener los siguientes métodos:
Frecuencia de Números.Dada la lista, devuelve un diccionario
con el número de veces que aparece cada número en la lista. Moda.Dada
la lista, devuelva la moda de la lista(el valor más repetido).Puedes usar la función anterior
como ayuda. Histograma.Dada la lista, muestra el histograma de la lista.
Puedes reusar los métodos anteriores.

Ejemplo:
lista = ListaNumeros([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
lista.histograma()

Salida:
1 ** ** *
2 ** ** **
3 ** **
4 **

Detección de Cambios en  Datos.
Imagina tener dos conjuntos de datos que representan el estado actual
y el estado anterior de un sistema.Crea una función que identifique los elementos que han cambiado
entre los dos conjuntos. Retorna un diccionario usando como la llave el estado anterior y como valor
el estado actual. Para este ejercicio pueden asumir que los datos son numéricos y / o cadenas.

Sistema de Reserva. Desarrolla un sistema de reservas utilizando sets. Crea conjuntos para
representar habitaciones disponibles y habitaciones reservadas en un hotel.Permite a los
usuarios realizar reservas, liberar habitaciones y mostrar la disponibilidad
actual.NOTA: No utilizar menú, solo las funciones, realizar las pruebas necesarias
para verificar funcionamiento adecuado.

Encriptación y Desencriptación de Mensajes Secretos.Tú y tu mejor amigo están creando un sistema
secreto para enviar mensajes entre ustedessin que nadie más pueda entenderlos.Deciden
utilizar un método de encriptación y desencriptación basado en listas o diccionarios.

Parte 1: Encriptación.Crear
una función llamada encriptar_mensaje
que tome como entrada un mensaje de texto y utilice un diccionario
para reemplazar cada letra por un código secreto.El diccionario de encriptación debe
asignar a cada letra una cadena de caracteres alfanuméricos aleatorios.Ejemplo de diccionario:
diccionario_encriptacion = {'a': '$%3', 'b': '8@*', 'c': '2&9', ...}

Parte2: Desencriptación.Crear una función llamada desencriptar_mensaje que tome como entrada un
mensaje encriptado y utilice el mismo diccionario para revertir el proceso y obtener el mensaje original.

Inventario de Productos.Gestiona un inventario de productos en una tienda utilizando
diccionarios.Las claves pueden ser los códigos de producto y los valores pueden ser diccionarios
con información como el nombre, precio y cantidad en stock.Debe tener funciones para
agregar, editar, eliminar producto, además de funciones para realizar venta e imprimir inventario."""

#Ejemplos:

#Duplicados.Desarrolle una función que dada una lista de números enteros, retorna True si al menos
#un valor aparece dos veces, y Falso si todos los elementos son distintos.

lis=[1,2,3,1,4]

s=set(lis)

if

#def Duplicados():
#num = [2, 2, 4, 1, 5, 6, ]

numbers = [1, 2, 3, 1, 5]
target = 7

#sum(index,value)
#for index,value in enumerate(nums):
    #if index
#aux{ }





nums = [3, 2, 4]
target = 6
busquedaSuma(nums, target)
(1, 2)

buplicados()

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha:
# Descripción:


#RETO: Intentar solucionar problema, solo con una línea de código dentro de la función.Sin contar el llamado
#y / o pruebas de las funciones.

#Suma de dos números.Dado una lista de números enteros y un valor entero(target), retorna el
#índice de los dos números que sumados sean igual al target.Debe asumir  que existe siempre
#una única solución, y que un mismo elemento no se puede usar dos veces.Debes retornar una tupla con los índices.

#def sumDosNumeros():


   # nums = [3, 2, 4]
    #target = 6
    #busquedaSuma(nums, target)
    #(1, 2)

#sumDosNumeros()

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha:
# Descripción:


# 3

def cui():
    t={}

    for c,p,z in ciudades:
        t[z]= t.get(z, 0) + p

    for  c,p,z in cuidades:
        densiPobla =  p/t[z]
        densiPobla[c]=





    #si k es igual a noroeste se acumula sum(k)s


    if
ciudades = [(“Tijuana”, 10, “NE”),
            (“Ciudad de Mexico”, 4, “Cen”),
            (“Ensenada”, 5, “NE”),
            (“Jalisco”, 8, “Cen”),
            (“tecate”, 4, “Sur”)]

for
densidades = calcular_densidades(ciudades)
mayor = mayor_densidad(ciudades)

print(densidades)
# {“Tijuana”: 0.62, “Ciudad de Mexico”: 0.72, “Ensenada”: 0.37, “Puebla”:0.27, “Cancun”: 4}

print(mayor)