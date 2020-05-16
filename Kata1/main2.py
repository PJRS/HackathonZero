"""
Crear un programa donde le pases un numero y te devuelva su 
tabla de multiplicar
"""
tabla = int(input("introduzca numero de la tabla a multiplicar: "))

#range(x) -> Empieza por 0 y el numero llega hasta x-1
#range(0,11,1)
for i in range(11):
    #print(i)
    print(str(tabla) + " x " + str(i) + " = "  + str(tabla*0))
