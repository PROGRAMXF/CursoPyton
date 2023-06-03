"""
escribir un programa que nos permita crear objetos de tipo productos con los atributos:
nombre, valor, descripcion, cantidad y que ademas nos permita agregar productos a la
lista y luego mostrarlos.
"""

class Producto: #creamos el objeto
    def __init__(self, nombre, valor, descripcion, cantidad): #parametros
        self.nombre = nombre
        self.valor = valor
        self.descripcion = descripcion
        self.cantidad = cantidad
    
c = int(input("¿Cuantos productos ingresara?: ")) 

productos =[] #lista vacia al comienzo

for i in range(c): #bucle for para que en funcion de la cantidad de productos que vamos a ingresar nos pide los parametros
    print("Producto numero: ", i+1)
    n = input("Nombre del producto: ")
    vr = int(input("Valor del producto: "))
    descripcion = input("Descripcion del producto: ")
    cantidad = int(input("Cantidad del producto: "))

    p = Producto(n, vr, cantidad, descripcion)
    productos.append(p) #nos ingresa los parametros del producto a traves de append


    print("********LISTADO DE PRODUCTOS*********")

    for j in range(len(productos)): #con otro bucle for nos muestra por pantalla los valores del producto
        print("Nombre: ", productos[j].nombre)
        print("Descripcion: ", productos[j].descripcion)
        print("Valor: ", productos[j].valor)
        print("Cantidad: ", productos[j].cantidad)
        print("********************************")