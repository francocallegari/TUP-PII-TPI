# Trabajo Práctico I - Programación II
# Alumnos: Basile Nicole,  Callegari Franco, Cechetto Juan Cruz

import os
import bibloteca

print("Bienvenido!")
respuesta = ''

def menu():
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolución")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            print("Gestionar préstamo de un libro:")
            bibloteca.prestar_ejemplar_libro()
            print()
        elif int(opt) == 2:
            print("Gestionar devolución de un libro:")
            bibloteca.devolver_ejemplar_libro()
            print()
        elif int(opt) == 3:
            print("Registro de nuevo libro:")
            bibloteca.registrar_nuevo_libro()
            print()
        elif int(opt) == 4:
            print("Eliminar un ejemplar de un libro:")
            bibloteca.eliminar_ejemplar_libro()
            print()
        elif int(opt) == 5:
            print("Lista de ejemplares prestados:")
            print("")
            bibloteca.ejemplares_prestados()
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")