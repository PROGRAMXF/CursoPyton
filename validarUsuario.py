"""
validar un usuario, caracteristicas:
longitud mayor a 6 caracteres y menores a 12
debe ser alfanumerico
"""

usuario = input("Ingrese el nombre del usuario:")
caracteres = len(usuario)
tipo = usuario.isalnum()
if tipo == True:
    if caracteres < 6:
        print("Se deben ingresar por lo menos 6 caracteres")

    elif( caracteres > 12):
        print("Se deben ingresar manores a 12 caracteres")

    else:
        print("Bienvenido", usuario)
else:
    print("Error, valor incorrecto ")