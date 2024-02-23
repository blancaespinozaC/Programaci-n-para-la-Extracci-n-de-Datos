#Primero

"""Duplicados.Desarrolle una función que dada una lista de números enteros, retorna True si al menos
#un valor aparece dos veces, y Falso si todos los elementos son distintos.
#RETO: Intentar solucionar problema, solo con una línea de código dentro de la función.Sin contar el llamado
#y / o pruebas de las funciones."""

def duplicados():
    lis = [1, 2,8, 3, 4, 5, 6, 7, 8]

    return len(lis) != len(set(lis))
resultado = duplicados()
print(resultado)

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha:17/02/2024
# Descripción: En este problema se realizo un codigo con una lista donde por el contenido de la lista
#saber si los numeros estan duplicados o no, asi al realizarlo nos muestra como resultado  True si hay duplicados
# y aparece False entomces todos los numero son distintos.

#___________________________________________________________________________________________________________________________
#Segundo
"""Suma de dos números.Dado una lista de números enteros y un valor entero(target), retorna el
#índice de los dos números que sumados sean igual al target.Debe asumir  que existe siempre
#una única solución, y que un mismo elemento no se puede usar dos veces.Debes retornar una tupla con los índices.
#RETO: Intentar solucionar problema como máximo usando un ciclo.Puedes usar variables, condiciones
#y / o estructuras auxiliares."""
def busquedaSuma():
    aux = {}

    for index, value in enumerate(nums):
        falta = target-value
        if falta in aux:
            return (aux[falta], index)
        aux[value] = index

nums = [2, 1, 11, 15, 7, 3,]
target = 9
print(busquedaSuma())

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 17/02/2024
# Descripción: En este problema tenemos un lista donde tenemos que realizar un codigo que sumando dos numero de la lista
#nos den un target y tambien tendro del codigo que no mande como resultado la posicion en la que estan los numero.

#_______________________________________________________________________________________________________________________
#Tercero
"""Análisis de Población.Tienes datos sobre población de diferentes ciudades representados como
#tuplas(ciudad, población, área).Crea funciones para:"""

# a. Calcular la densidad de población (población dividida por la cantidad total de población por área) para cada ciudad.
def calcular_la_densidad(ciudades):
    total = {}

    for ciudad, poblacion, area in ciudades:
        total[area] = total.get(area, 0) + poblacion

    densidad = {}

    for ciudad, poblacion, area in ciudades:
        densidad_poblacion = poblacion / total[area]
        densidad[ciudad] = densidad_poblacion

    return densidad, total

# b. Identificar la ciudad con la mayor densidad de población.
def mayor_densidad(ciudades, total):
    ciudadMayor = ""
    madensidad = 0

    for ciudad, poblacion, area in ciudades:
        densidad_poblacion = poblacion / total[area]
        if densidad_poblacion > madensidad:
            madensidad = densidad_poblacion
            ciudadMayor = ciudad

    return ciudadMayor

ciudades = [
    ("Tijuana", 10, "NE"),
    ("Ciudad de Mexico", 8, "CEN"),
    ("Ensenada", 5, "NE"),
    ("Puebla", 3, "CEN"),
    ("Cancun", 8, "SUR")
]

# Llamada a la función para calcular la densidad y obtener el total
densidades, total = calcular_la_densidad(ciudades)

# Llamada a la función para identificar la ciudad con la mayor densidad
mayor = mayor_densidad(ciudades, total)

print(densidades)
print(mayor)
#Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 18/02/2024
# Descripción: En este problema tenemos un lista donde tenemos que realizar un codigo que sumando dos numero de la lista
#nos den un target y tambien tendro del codigo que no mande como resultado la posicion en la que estan los numero.


#Cuarto
print("------------------------------------------------------------------------------")
"""Estadística Básica.Cree una clase llamada Estadística que contiene como atributo una
lista de números naturales la cual puede contener repetidos.
Debe contener los siguientes métodos:
Frecuencia de Números.Dada la lista, devuelve un diccionario
con el número de veces que aparece cada número en la lista. Moda.Dada
la lista, devuelva la moda de la lista(el valor más repetido).Puedes usar la función anterior
como ayuda. Histograma.Dada la lista, muestra el histograma de la lista.
Puedes reusar los métodos anteriores."""

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def frecuencia_numeros(self):
        frecuencia = {}
        for num in self.numeros:
            frecuencia[num] = frecuencia.get(num, 0) + 1
        return frecuencia

    def moda(self):
        frecuencia = self.frecuencia_numeros()
        moda = max(frecuencia, key=frecuencia.get)
        return moda

    def histograma(self):
        frecuencia = self.frecuencia_numeros()
        for num, count in frecuencia.items():
            print(f"{num}: {'*' * count}")

# Ejemplo de uso
lista_numeros = [8, 3, 2, 4, 2, 2, 3, 2, 4, 8, 2, 1, 2, 3, 1, 3, 1]
estadistica = Estadistica(lista_numeros)

print("Frecuencia de Números:", estadistica.frecuencia_numeros())
print("Moda:", estadistica.moda())
print("Histograma:")
estadistica.histograma()
#Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 19/02/2024
# Descripción: En este codigo de una secuencia de numeros en el cual el codigo realiza 3 clases en el cual nos muentra
#la frecuencua, la moda de los numero y tambien un pequeño histograma donde mientra con arteriscos cuantas veces se
#repite el numero.

print("__________________________________________________________________________")

#Quinto
"""Detección de Cambios en  Datos.
Imagina tener dos conjuntos de datos que representan el estado actual
y el estado anterior de un sistema.Crea una función que identifique los elementos que han cambiado
entre los dos conjuntos. Retorna un diccionario usando como la llave el estado anterior y como valor
el estado actual. Para este ejercicio pueden asumir que los datos son numéricos y / o cadenas."""


def detectar_cambios(estado_anterior, estado_actual):
    cambios = {}

    for clave, valor_anterior in estado_anterior.items():
        if clave in estado_actual:
            valor_actual = estado_actual[clave]
            if valor_anterior != valor_actual:
                cambios[clave] = valor_actual

    return cambios

estado_anterior = {'a': 1, 'b': 2, 'c': 3}
estado_actual = {'a': 1, 'b': 7, 'c': 3, 'd': 4}

resultado_cambios = detectar_cambios(estado_anterior, estado_actual)
print("Cambios detectados: ", resultado_cambios)

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 21/02/2024
# Descripción: En este codigo se realiza  dos conjuntos de datos datos uno actual y el otro anterio en que
#se hace un ciclo para saber si hay un cambio en el conjunto actual y el conjunto anterior si hay cambio, ]
#se almacena en un diccionario aparte y eso es lo que se muentra en el resultado.

#6
"""Sistema de Reserva. Desarrolla un sistema de reservas utilizando sets. Crea conjuntos para
representar habitaciones disponibles y habitaciones reservadas en un hotel.Permite a los
usuarios realizar reservas, liberar habitaciones y mostrar la disponibilidad
actual.NOTA: No utilizar menú, solo las funciones, realizar las pruebas necesarias
para verificar funcionamiento adecuado."""

habitaciones_disponibles = set(range(1, 8))
habitaciones_reservadas = set()

def realizar_reserva(habitacion):
    global habitaciones_disponibles, habitaciones_reservadas
    if habitacion in habitaciones_disponibles:
        habitaciones_disponibles.remove(habitacion)
        habitaciones_reservadas.add(habitacion)

        print("Habitación reservada con éxito: ", habitacion)
    else:
        print("Habitación no disponible: ", habitacion)

def liberar_habitacion(habitacion):
    global habitaciones_disponibles, habitaciones_reservadas
    if habitacion in habitaciones_reservadas:
        habitaciones_reservadas.remove(habitacion)
        habitaciones_disponibles.add(habitacion)

        print("Habitación liberada: ",habitacion)
    else:
        print("Habitación no estaba reservada: ",habitacion)

def mostrar_disponibilidad():
    global habitaciones_disponibles, habitaciones_reservadas
    print("Habitaciones Disponibles:", habitaciones_disponibles)
    print("Habitaciones Reservadas:", habitaciones_reservadas)

#pruebas
realizar_reserva(3)
realizar_reserva(4)
liberar_habitacion(6)
mostrar_disponibilidad()
# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 20/02/2024
# Descripción: En este codigo se realiza una reservacion para una habitación especificadas
# en el que se muentra si las habitación estás disponibles, tambien se muestran las habitaciones reserlvadas, y las que no estan.

#7
"""Parte 1: Encriptación.Crear
una función llamada encriptar_mensaje
que tome como entrada un mensaje de texto y utilice un diccionario
para reemplazar cada letra por un código secreto.El diccionario de encriptación debe
asignar a cada letra una cadena de caracteres alfanuméricos aleatorios.Ejemplo de diccionario:
diccionario_encriptacion = {'a': '$%3', 'b': '8@*', 'c': '2&9', ...}"""


def encriptar_mensaje(mensaje, diccionario):
    mensaje_encriptado = ""
    for letra in mensaje:
        if letra in diccionario:
            mensaje_encriptado = mensaje_encriptado + diccionario[letra]
        else:
            mensaje_encriptado = mensaje_encriptado + letra
    return mensaje_encriptado



"""Parte2: Desencriptación.Crear una función llamada desencriptar_mensaje que tome como entrada un
mensaje encriptado y utilice el mismo diccionario para revertir el proceso y obtener el mensaje original."""

def desencriptar_mensaje(mensaje_encriptado, diccionario):
    #diccionario = {codigo: letra for letra, codigo in diccionario.items()}
    mensaje_desencriptado = ""
    for codigo in mensaje_encriptado:
        if codigo in diccionario:
            mensaje_desencriptado = mensaje_desencriptado + diccionario[codigo]
        else:
            mensaje_desencriptado = mensaje_desencriptado + codigo
    return mensaje_desencriptado

diccionario = {'a': '$%3', 'b': '8@*', 'c': '2&9', 'd': '3#5', 'e': '!4$', 'f': '6*4', 'g': '^%8', 'h': '5@2', 'i': '4&5', 'j': '#7!', 'k': '*3^', 'l': '$%9', 'm': '@2&', 'n': '&9@', 'o': '7!$', 'p': '3^*', 'q': '2$%', 'r': '2@9', 's': '8#', 't': 'a!7', 'u': '6*4', 'v': '8^$', 'w': '5&9', 'x': '4!o', 'y': 'p#1', 'z': 'm*3', ' ': ' '}

mensaje_original = "Hola, mundo!"
mensaje_encriptado = encriptar_mensaje(mensaje_original, diccionario)
mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado, diccionario)

print("Mensaje Original:", mensaje_original)
print("Mensaje Encriptado:", mensaje_encriptado)
print("Mensaje Desencriptado:", mensaje_desencriptado)
# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 20/02/2024
#Descripcion: En este codigo se desprende un mensaje utilizando un diccionario de encriptación.
#Esto corresporque se reemplaza cada letra del mensaje con un código que esta diccionario que apregamos.
#En el cual si la letra no está en el diccionario, se deja como esta originalemnte.
#La segunda parte del codigo se desencripta el mensaje encriptado utilizando el mismo diccionario.
#esto revierte el proceso de encriptación de la primera parte para obtener el mensaje original,
#Y al final si el código no está en el diccionario, se deja sin cambios.

#8
"""Inventario de Productos.Gestiona un inventario de productos en una tienda utilizando
diccionarios.Las claves pueden ser los códigos de producto y los valores pueden ser diccionarios
con información como el nombre, precio y cantidad en stock.Debe tener funciones para
agregar, editar, eliminar producto, además de funciones para realizar venta e imprimir inventario."""
inventario = {}

def agregar_producto(codigo, nombre, precio, cantidad):
    if codigo in inventario:
        inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print(f"Producto agregado al inventario es: ", nombre)
    else:
        print(f"El producto con el código ya existe en el inventario: ", codigo)

def editar_producto(codigo, nombre, precio, cantidad):
    if codigo in inventario:
        inventario[codigo] = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        print(f"Producto  editado en el inventario es: ", nombre)
    else:
        print(f"No se encontró el producto con código {codigo} en el inventario.")

def eliminar_producto(codigo):
    if codigo in inventario:
        del inventario[codigo]
        print(f"Producto con código  eliminado del inventario es: ", codigo)
    else:
        print(f"No se encontró el producto con código {codigo} en el inventario.")

def realizar_venta(codigo, cantidad):
    if codigo in inventario:
        if inventario[codigo]["cantidad"] >= cantidad:
            inventario[codigo]["cantidad"] -= cantidad
            print(f"Venta realizada. Stock actualizado para el producto {inventario[codigo]['nombre']}.")
        else:
            print(f"No hay suficiente stock para el producto {inventario[codigo]['nombre']}.")
    else:
        print(f"No se encontró el producto con código {codigo} en el inventario.")

def imprimir_inventario():
    print("\nInventario Actual:")
    for codigo, producto in inventario.items():
        print(f"Código: {codigo}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()

# Ejemplo de uso con datos diferentes
agregar_producto("P101", "Zapatillas", 49.97, 20)
agregar_producto("P102", "Reloj", 99.50, 10)
imprimir_inventario()

editar_producto("P101", "Zapatillas Deportivas", 59.99, 15)
imprimir_inventario()

realizar_venta("P102", 5)
imprimir_inventario()

eliminar_producto("P103")

# Nombre: BLANCA ISABEL ESPINOZA CRUZ
# Grupo: 951
# Fecha: 21/02/2024
#Descripcion: Es este codigo se hace un inventacion en codigo en el cual por varios def se puedes saber el nombre, precio, cantidad y stock
#del inventario, dentro del codigo hay un parte para agregar informacion del producto, tambien de para agregar un producto,
# tambien para editar el producto, y al final se impirme el resulyado, como tambine realizar el producto de ventas,
# y al final nos muenstra el resultado del producto eliminado

