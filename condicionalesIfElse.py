#hacer un programa para calcular el total a pagar por una compra de camisas. Si se compran
#tres camisas o mas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres del 10%

print("Ingrese la cantidad de camisas compradas: ")
cant = int(input())
print("Ingrese el valor de cada camisa")
vr = int(input())
desc = 0

sub = cant * vr
if(cant>=3):
    desc = sub*0.2
    print("Su descuento fue del 20%")
else:
    desc = sub*0.1    
    total =sub-desc
    print("Su descuento fue del 10%")

print("El total a pagar es : ",total)
print("El descuento otorgado es de: ",desc)


