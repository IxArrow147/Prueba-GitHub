"""
1.	Crea una lista con todos los países de Latinoamérica y otra lista con sus respectivas poblaciones, con base a esto vas a generar:
a)	un listado de países con las poblaciones mayores a 20 millones de habitantes.
b)	un listado de países con las poblaciones mayores a 20 millones de habitantes.
"""

# Limpiar terminal
import os

def limpiar_terminal():
    os.system("cls")

limpiar_terminal()

#Conjuntos
# Lista con los nombres de los paises.
paises = [
    "Argentina", "Bolivia", "Brasil", "Chile", "Colombia",
    "Costa Rica", "Cuba", "Ecuador", "El Salvador", "Guatemala",
    "Haití", "Honduras", "México", "Nicaragua", "Panamá",
    "Paraguay", "Perú", "República Dominicana", "Uruguay", "Venezuela"
]

# Lista con la población correspondiente a cada país.
# La posición de cada población coincide con la del país en la lista anterior.
poblacion = [
    47000000, 12000000, 212000000, 20000000, 53000000,
    5300000, 9700000, 18000000, 6300000, 18000000,
    11500000, 10000000, 130000000, 7000000, 4500000,
    6800000, 34000000, 11500000, 3500000, 28000000
]

# Se crea un diccionario mediante una comprehension
# zip() une cada país con su población y solo se guardan
# aquellos cuya población es mayor a 20 millones.
dict_mayores_20M = {i: j for i, j in zip(paises, poblacion) if j > 20000000}

print("Los países con población mayor a 20 millones de habitantes son:")
# Se recorren las claves del diccionario para mostrar los paises
for i in dict_mayores_20M:
    print(f"-- {i}")

print()

# Se crea un segundo diccionario con los países cuya población
# es menor a 20 millones de habitantes.
dict_menores_20M = {i: j for i, j in zip(paises, poblacion) if j < 20000000}
# Se recorren las claves del diccionario para mostrar los paises
print("Los países con población menor a 20 millones de habitantes son:")
for i in dict_menores_20M:
    print(f"-- {i}")