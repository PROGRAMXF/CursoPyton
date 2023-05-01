"""como manejar los strings"""

print("calle 9 de julio")
print('calle 9 de julio')

#usamos tanto comillas dobles como simples

direccion = "calle 9 de julio"
print("La direccion es: ", direccion)

print("La direccion es : ", direccion[2]) #con indice 2 nos muestra la letra l

print(len(direccion)) #mediante la funcion len nos muestra la longitud de los caracteres

#con condicionales:
if "8" in direccion:
    print("Se encontro el valor")
else:
    print("No se encontro el valor")