"""
pedir una nota de 0 a 10 y mostrarla de forma:
Insuficiente: si esta entre 0 y 5
Aceptable: si es igual a  5
Sobresaliente: si es mayor a 5 y menor a 9
Excelente: si es igual a 10

"""
print("Ingrese una nota para verificar: ")
nota = int(input())

if(nota >= 0 and nota < 5):
    print("La nota es insuficiente")

elif(nota == 5):
    print("La nota es Aceptable")

elif(nota > 5 and nota < 9):
    print("La nota es Sobresaliente")

elif(nota == 10 ):
    print("La nota es Excelente")

else:
    print("El valor ingresado no es valido")

    
