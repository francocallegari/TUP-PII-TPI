import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def ejemplares_prestados():
    for libro in libros:
        cod = libro["cod"]
        cant_ej_ad = libro["cant_ej_ad"]
        cant_ej_pr = libro["cant_ej_pr"]
        titulo = libro["titulo"]
        autor = libro["autor"]

        if cant_ej_pr == 1:
            print(f"{titulo} de {autor} tiene {cant_ej_pr} ejemplar prestado")
        elif cant_ej_pr > 1:
            print(f"{titulo} de {autor} tiene {cant_ej_pr} ejemplares prestados")
        else:
            print(f"{titulo} de {autor} no tiene ejemplares prestados")
    
    return None
            
def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()

    libros.append(nuevo_libro)

    cod = nuevo_libro["cod"]
    cant_ej_ad = nuevo_libro["cant_ej_ad"]
    titulo = nuevo_libro["titulo"]
    autor = nuevo_libro["autor"]

    print("Nuevo libro registrado:")
    print(f"Nombre: {titulo}\nAutor: {autor}\nCódigo: {cod}\nEjemplares adquiridos: {cant_ej_ad}")

    return None

def eliminar_ejemplar_libro():
    ver_listado_libros()

    codigo_buscar = str(input("Ingrese el codigo del libro a buscar: "))
    bandera = 0

    for libro in libros:
        cod = libro["cod"]

        if codigo_buscar == cod:
            
            if libro["cant_ej_ad"] > 0:
                libro["cant_ej_ad"] -= 1
                bandera = 2
            else:
                bandera = 1

    if bandera == 2:
        print(f"El ejemplar del libro con código {codigo_buscar} fue eliminado exitosamente.")
    elif bandera == 1:
        print(f"El libro con código {codigo_buscar} no posee ejemplares adquiridos.")
    else:
        print(f"No exite libro con código {codigo_buscar}")

    return None


def prestar_ejemplar_libro():
    ver_listado_libros()

    codigo_buscar = str(input("Ingrese el codigo del libro a buscar: "))
    bandera = 0

    for libro in libros:
        cod = libro["cod"]

        if codigo_buscar == cod:
            bandera = 1
            cant_ej_ad = libro["cant_ej_ad"]
            cant_ej_pr = libro["cant_ej_pr"]
            titulo = libro["titulo"]
            autor = libro["autor"]
            
            ejemplares_disponibles = cant_ej_ad - cant_ej_pr
            print(f"Autor: {autor}\nNombre: {titulo}\nCantidad de ejemplares disponibles: {ejemplares_disponibles}")

            if ejemplares_disponibles == 0:
                print("No quedan ejemplares para prestar.")
            else:
                confirmar_prestamo = None
                while confirmar_prestamo not in ["si", "no"]:
                    confirmar_prestamo = str(input("¿Desea confirmar el prestamo? Ingrese Si o No: ").lower())
                    if confirmar_prestamo == "si":
                        print("El prestamo fue realizado con éxito.")
                        libro["cant_ej_pr"] += 1
                    elif confirmar_prestamo == "no":
                        print("Prestamo cancelado.")
                    else:
                        print("Opción no válida. Por favor, ingrese 'Si' o 'No'.")
            break
  
    if bandera == 0:
        print(f"No existe libro con código {codigo_buscar}")

    return None


def devolver_ejemplar_libro():
    ver_listado_libros()

    codigo_buscar = str(input("Ingrese el codigo del libro a buscar: "))
    bandera = 0

    for libro in libros:
        cod = libro["cod"]
        ej_prestados = libro["cant_ej_pr"]
        titulo = libro["titulo"]
        autor = libro["autor"]

        if codigo_buscar == cod and ej_prestados > 0:
            bandera = 2
            print(f"Código: {cod} - Nombre: {titulo} - Autor: {autor}")
            confirmar_devolucion = None
            while confirmar_devolucion not in ["si", "no"]:
                confirmar_devolucion = str(input("¿Desea confirmar la devolución? Ingrese Si o No: ").lower())
                if confirmar_devolucion == "si":
                    libro["cant_ej_pr"] -= 1
                    print("La devolución fue realizado con éxito.")
                
                elif confirmar_devolucion == "no":
                    print("Devolución cancelada.")
                else:
                    print("Opción no válida. Por favor, ingrese 'Si' o 'No'.")
            break
        elif codigo_buscar == cod and not ej_prestados:
            bandera = 1
            break


    if bandera == 1:
        print(f"El libro con código {codigo_buscar} no tiene ejemplares prestados.")
    elif bandera == 0:
        print(f"No existe libro con código {codigo_buscar}")

    return None

def nuevo_libro(): #No fue utilizada, se uso la función del archivo libro.py
    #completar
    return None

def ver_listado_libros(): #Funcion para ver listado de libros
    ver_lista = str(input("¿Desea ver el listado de libros? Ingrese Si o No: ").lower())
    if ver_lista == "si":
        for libro in libros:
            cod = libro["cod"]
            cant_ej_ad = libro["cant_ej_ad"]
            cant_ej_pr = libro["cant_ej_pr"]
            titulo = libro["titulo"]
            autor = libro["autor"]
            print(f"{cod}, {titulo}, {autor}, {cant_ej_ad}, {cant_ej_pr}")
    elif ver_lista == "no":
        print()
    else:
        print("Opción no válida. Por favor, ingrese 'Si' o 'No'.")
    
    return None