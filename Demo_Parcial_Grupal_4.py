#Suma de enteros y de pares

print ("Suma de enteros y de sus impares")
x=int(input())
y=int(input())
print ("*"*50)
cont=0
i=0
acum=0
#Enteros
for i in range (x,y+1,1):
    acum+=i
print ("La suma de los números enteros es {}".format(acum))

#Impares
if x%2==0: 
    for i in range (x,y+1,2):
        cont+=i
    print ("A.La suma de los pares que empiezan en {} y terminan en {} es {}".format(x,y,cont))
else:
    for i in range (x+1,y,2):
        cont+=i
    print ("B.La suma de los pares que empiezan en {} y terminan en {} es {}".format(x,y,cont))

    
