import random #libreria para crear numeros randoms

numeros=[]#coleccion vacia
for i in range(100): #ciclo para repetir 100 veces
    numeros.append(random.randint(1,100))#guardamos en la lista el numero aleatorio

numero=random.randint(1,100) #rango para el numero random

numeros.sort()#ordenar de menor a mayor
print(numeros)