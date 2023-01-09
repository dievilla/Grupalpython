#Para el valor min o max
cant=int(input("Ingrese la cantidad de valores: "))
min=9999

for i in range (cant):
    numero=float(input("Ingrese el número:  "))
    print ("")
    if numero<min:
        min=numero
print ("El menor número es: ",min)
