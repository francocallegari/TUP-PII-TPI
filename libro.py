import cod_generator

# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    #completar
    cod = generar_codigo()
    while True:
        try: #Con try logro forzar que el usuario si o si ingrese una cantidad valida 
            cant_ej_ad = int(input("Ingrese la cantidad de ejemplares adquiridos: "))
            break
        except:
            print("Ingrese una cantidad valida")
    while cant_ej_ad < 1:
        cant_ej_ad = int(input("Ingrese un número válido: "))
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")

    agregar_libro = {'cod': cod, 'cant_ej_ad': cant_ej_ad, 'cant_ej_pr': 0, "titulo": titulo, "autor": autor}
    return agregar_libro

def generar_codigo():
    #completar
    cod = cod_generator.generar()
    return cod