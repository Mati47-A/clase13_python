import random #libreria para crear numeros randoms

numeros=[]#coleccion vacia
for i in range(100): #ciclo para repetir 100 veces
    numeros.append(random.randint(1,100))#guardamos en la lista el numero aleatorio

numero=random.randint(1,100) #rango para el numero random

numeros.sort()#ordenar de menor a mayor
print(numeros)#mostrar lista

#contador de numeros pares
contador=0
for i in range (len(numeros)):
    if numeros[i]%2==0: #%=el resto de una division
        contador+=1
print(f"cantidad de numeros pares : {contador}")