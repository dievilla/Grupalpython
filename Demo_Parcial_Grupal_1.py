#Promedio

print ("Programa para hallar Nº números")
var1=int(input("Ingrese la cantidad de elementos: "))
suma=0
i=1
while i<=var1:
    print ("Ingrese su número",i)
    num2=float(input())
    suma=suma+num2
    i+=1
prom=suma/var1
print ("El resultado es {}".format(prom))