"""
Escribir un programapara calcular a pagar en una factura
de 3 productos, incluyendo IVA. Al final se debe mostrar 
los nombres de cada producto; el valor a pagar por cada 
uno de ellos y el total de la factura.
"""

print("Ingrese el nombre del primer producto:")
p1 = input()
print("Cantidad comprada del primer producto: ", p1)
p1_cant = int(input())
print("Valor de la unidad: ", p1)
p1_val = int(input())

print("Ingrese el nombre del segundo producto:")
p2 = input()
print("Cantidad comprada del primer producto: ", p2)
p2_cant = int(input())
print("Valor de la unidad: ", p2)
p2_val = int(input())

print("Ingrese el nombre del tercer producto:")
p3 = input()
print("Cantidad comprada del primer producto: ", p3)
p3_cant = int(input())
print("Valor de la unidad: ", p3)
p3_val = int(input())

#operaciones:
p1_st = p1_cant * p1_val
p2_st = p2_cant * p2_val
p3_st = p3_cant * p3_val

subTotal = p1_st + p2_st + p3_st

#Calculamos el IVA:

Iva = subTotal * 0.21
Total = subTotal + Iva

#salidas:
print("El total a pagar por: ", p1, "es: ", p1_st)
print("El total a pagar por: ", p2, "es: ", p2_st)
print("El total a pagar por: ", p3, "es: ", p3_st)

print("El subtotal de la factura es : ", subTotal)
print("El Iva fue de: ", Iva)
print("El total a pagar con Iva fue de: ", Total)
