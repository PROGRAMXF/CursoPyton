"""
calcular el total a pagar por una venta de N
se debe mostrar:
IVA, subtotal y total
"""

print("Ingresar la cantidad de productos")
prod = int(input())

i = 0
sub = 0

while i<prod:
    print("Producto ",i+1, " valor: ")
    val = int(input())

    print("Cantidad")
    cant = int(input())

    subpro = val * cant
    sub = sub + subpro

    i+=1

    #calculamos el iva
    iva = sub * 0.19
    total = sub + iva

    print("Se vendieron: ", prod, "productos")
    print("Subtotal: ", sub)
    print("IVA", iva)
    print("Total: ", total)
