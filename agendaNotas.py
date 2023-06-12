notas = {}

def agregar_nota(notas, titulo, contenido): #funcion que recibe tres parametros
    notas[titulo] = contenido

def ver_notas(notas):
    if not notas:
        print("No hay notas para mostrar")

    else:
        for titulo, contenido in notas.items():
            print(f"--- {titulo} ---")
            print(contenido)
            print("--------------------------")

def editar_nota(notas, titulo, nuevo_contenido):
    if titulo in notas:
        notas[titulo] = nuevo_contenido
        print("La nota fue editada correctamente")
    else:
        print("No se encontro la nota especificada")

def eliminar_nota(notas, titulo):
    if titulo in notas:
        del notas[titulo] 
        print("La nota fue eliminada correctamente")
    else:
        print("La nota fue eliminada de manera correcta")
while True:
    print("-----Gestor de notas y apuntes-----")
    print("1. Agregar nota")
    print("2. Ver notas")
    print("3. Editar notas")
    print("4. Eliminar notas")
    print("5. Salir")

    opcion = input("Ingrese su opcion: ")


    if opcion == 1:
        titulo = input("Agrege el titulo de la nota")
        contenido = input("Ingrese el contenido de la nota")
        agregar_nota(notas, titulo, contenido)
        print("La nota se agrego correctamente")

    elif opcion == 2:
        ver_notas(notas)

    elif opcion == 3:
        titulo = input("Ingrese el titulo de la nota a editar")
        nuevo_contenido = input("Ingrese el nuevo contenido de la nota: ")
        editar_nota(notas, titulo, nuevo_contenido)

    elif opcion == 4:
        titulo = input("Ingrese el titulo de la nota a eliminar: ")
        eliminar_nota(notas, titulo)

    elif opcion == "5":
        break

    else:
        print("Opcion ingresada invalida")

    print("Fin del programa")




                  


            