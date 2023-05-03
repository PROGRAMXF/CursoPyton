edad = int(input("Ingrese su edad: "))

if(edad>=18 ): #en python estos dos puntos serian como las llaves en otros lenguajes de prog
    print("Es mayor de edad")
elif (edad<18):
    print("Es menor de edad")
    if(edad>60):
        print("Es jubilado")
else:
    print("Error, ingreso una edad negativa")