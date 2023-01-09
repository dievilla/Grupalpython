#Hacer un programa que muestre si un número es divisible por 3 o 5

print ("Ingrese el número a comprobar")
x=int(input())
if x//5==x/5:
    print ("El número es divisible entre 5")
elif x//3==x/3:
    print ("El número es divisible entre 3")

else:
    print ("El número no es divisible entre 5 ni 3")
 