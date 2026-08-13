"""
1. Escribe una función analizar_estudiantes (estudiantes1, estudiantes2) que reciba dos conjuntos de nombres de estudiantes. La función deberá retornar un diccionario con la siguiente información:


a. Un conjunto de estudiantes que están en ambos grupos.

b. Un conjunto de estudiantes que están solo en el primer grupo.

c. Un conjunto de estudiantes que están solo en el segundo grupo.

d. Un conjunto de todos los estudiantes.
"""

# limpiar la terminal
import os

def limpiar_terminal():
    os.system("cls")

limpiar_terminal()

def analizar_estudiantes(estudiantes1,estudiantes2,estudiantes3):# funcion que recibe dos conjuntos de estudiantes y devuelve un diccionario con los resultados del analisis.
      
       estudiantes1={i.title() for i in estudiantes1} # set comprehension convierte los nombres a minusculas dejando solo la primera letra en Mayuscula
       estudiantes2={i.title() for i in estudiantes2} # set comprehension convierte los nombres a minusculas dejando solo la primera letra en Mayuscula
       estudiantes3={i.title() for i in estudiantes3} # set comprehension convierte los nombres a minusculas dejando solo la primera letra en Mayuscula

       # calculos de los conjuntos.

       # 1 intersección de los dos conjuntos 
       interseccion=estudiantes1&estudiantes2&estudiantes3 
       # 2 diferencia solo los que esta en el grupo 1
       solo_en_grupo_1 = estudiantes1 - (estudiantes2 | estudiantes3)
       # 3 diferencia solo los que estan en el grupo 2
       solo_en_grupo_2 = estudiantes2 - (estudiantes1 | estudiantes3)
       # 4 diferencia solo los que estan en el grupo 3
       solo_en_grupo_3 = estudiantes3 - (estudiantes1 | estudiantes2)
       # 5 todos los estudiantes
       todos=estudiantes1|estudiantes2|estudiantes3
       # devuelve un diccionario con los resultados
       return { 
              "interseccion":interseccion,
              "solo_en_grupo_1":solo_en_grupo_1,
              "solo_en_grupo_2":solo_en_grupo_2,
              "solo_en_grupo_3":solo_en_grupo_3,
              "todos":todos

       }

def ingreso_estudiantes(): # funcion para ingresar los nombres de los estudiantes, valida que no esten vacios y que no contengan numeros.
       estudiantes=set() # conjunto vacio para almacenar los nombres de los estudiantes.
       i=1 # contador para el numero de estudiante
       while True: # bucle infinito para ingresar los nombres de los estudiantes, se rompe cuando el usuario ingresa "fin"
              try: # bloque try para capturar errores de entrada de datos
                     nombre = input(f"Ingrese el nombre del estudiante número {i}. Si no desea ingresar más estudiantes, escriba 'fin': ").strip() # strip() elimina los espacios en blanco al inicio y al final del nombre.
                     if nombre.lower()=="fin": # la funcion lower() convierte el nombre a minusculas para que no importe si el usuario ingresa "fin" o "FIN"
                            break  # rompe el bucle si el usuario ingresa "fin"
                     if not nombre:# valida que el nombre no este vacio
                            print("El nombre no debe estar vacio, intentelo de nuevo: ")
                            continue # continua con el bucle si el nombre esta vacio
                     if any(char.isdigit() for char in nombre): # valida que el nombre no contenga numeros, la funcion any() devuelve True si algun caracter es un numero.
                            print("El nombre no debe contener numeros, digitelo nuevamente") 
                            continue
                     if not nombre.replace(" ", "").isalpha():#Valida que solo tenga letras y no caracteres raros como @ # etc.
                            print("El nombre solo debe contener letras.")
                            continue           
              except ValueError: # captura el error de entrada de datos y muestra un mensaje de error
                     print("Digite una opcion valida")
              estudiantes.add(nombre.title())# funcion add para agregar elementos a un conjunto, no se permiten duplicados y ademas Corrige si una persona Dijita JUAN o juan, aparecera como Juan
              i+=1
       return estudiantes  # devuelve el conjunto de estudiantes ingresados por el usuario.
                     
                            
              
                     
# codigo principal
if __name__=="__main__": # bloque principal del programa, se ejecuta solo si el archivo es ejecutado directamente.
       limpiar_terminal() # limpia la terminal al inicio del programa
       print("\n---Ingreso estudiantes del grupo 1---\n")# mensaje para el usuario
       estudiantes1=ingreso_estudiantes()# llama a la funcion ingreso_estudiantes() para ingresar los nombres de los estudiantes del grupo 1
       print("---Los integrantes del grupo 1 son: ") # mensaje para el usuario
       for i in estudiantes1:#bucle for para mostrar los nombres de los estudiantes del grupo 1
              print(f"-{i}") # muestro todos los estudiantes del grupo 1
       
       print("\n---Ingreso estudiantes del grupo 2---\n")# mensaje para el usuario
       estudiantes2=ingreso_estudiantes()# llama a la funcion ingreso_estudiantes() para ingresar los nombres de los estudiantes del grupo 2
       print("\n---Los integrantes del grupo 2 son: ")# mensaje para el usuario
       for i in estudiantes2:#bucle for para mostrar los nombres de los estudiantes del grupo 2
              print(f"-{i}") # muestro todos los estudiantes del grupo 2
       
       print("\n---Ingreso estudiantes del grupo 3---\n")# mensaje para el usuario
       estudiantes3=ingreso_estudiantes()# llama a la funcion ingreso_estudiantes() para ingresar los nombres de los estudiantes del grupo 2
       print("\n---Los integrantes del grupo 3 son: ")# mensaje para el usuario
       for i in estudiantes3:#bucle for para mostrar los nombres de los estudiantes del grupo 3
              print(f"-{i}") # muestro todos los estudiantes del grupo 3

       #MOSTRAR
       # Resultados del analisis de los estudiantes y muestro los resultados en la terminal
       print()
       print(40*"=")
       print("El resultado del analisis es: ")
       print(40*"=")

       #Estudiantes en los 3 Grupos
       print("\nEstudiantes en los 3 Grupos")
       resultado=analizar_estudiantes(estudiantes1,estudiantes2,estudiantes3)
       if resultado["interseccion"]:
              for i in sorted(resultado["interseccion"]): # La funcion Sorted sirve para simplemente devolver un lista ordenada
                     print(f"- {i}")
       else:
              print("\nNo hay estudiantes que pertenezcan a los tres grupos.") # muestro uno debajo del otro los estudiantes que estan en 3 grupos
       
       print(40*"=")
       print(40*"=")

       #Solo en el Primer Grupo
       print("Conjunto de estudiantes que están solo en el primer grupo")
       if resultado["solo_en_grupo_1"]:
              for i in sorted(resultado["solo_en_grupo_1"]):
                     print(f"- {i}")
       else:
              print("\nNo hay estudiantes que pertenezcan únicamente al primer grupo.")# muestro los estudiantes que estan solo en el grupo 1
       print(40*"=")
       print(40*"=")

       #Solo en el Segundo Grupo
       print("Conjunto de estudiantes que están solo en el segundo grupo")
       if resultado["solo_en_grupo_2"]:
              for i in sorted(resultado["solo_en_grupo_2"]):
                     print(f"- {i}")
       else:
              print("\nNo hay estudiantes que pertenezcan únicamente al segundo grupo.")# muestro los estudiantes que estan solo en el grupo 2
       print(40*"=")
       print(40*"=")

       #Solo en el Tercer Grupo
       print("Conjunto de estudiantes que están solo en el tercer grupo")
       if resultado["solo_en_grupo_3"]:
              for i in sorted(resultado["solo_en_grupo_3"]):
                     print(f"- {i}")
       else:
              print("\nNo hay estudiantes que pertenezcan únicamente al tercer grupo.")# muestro los estudiantes que estan solo en el grupo 3
       print(40*"=")
       print(40*"=")

       #Todos los estudiantes
       print("Todos los estudiantes")
       if resultado["todos"]:
              for i in sorted(resultado["todos"]):
                     print(f"- {i}")
       else:
              print("\nNo hay estudiantes registrados.")# muestro todos los estudiantes
       print(40*"=")
       print(40*"=")

       #Prueba


       #Prueba