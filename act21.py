import random #libreria para crear numeros randoms
#import random import randint

numeros=[]
for i in range(100): 
    numeros.append(random.randint(0,10))

print(numeros)

for i in range (len(numeros)):
    if i%2==0: #solo se muestran numeros pares
        print(f"[{i}] : {numeros[i]}")

#mostrar numero mas alto
mayor=max(numeros)
print(f"numero mas alto : {mayor}")

#Mostrar el índice (posición) del elemento mayor
print("indices donde se encuentra el numero mayor")
for i in range(len(numeros)):
    if numeros[i]==max(numeros):
        print(i, end=" - ")
print(" ")
#Mostrar el elemento menor
menor=min(numeros)
print(f"numero menor : {menor}")

#Mostrar el índice del elemento menor
print("indices donde se encuentra el numero menor")
for i in range(len(numeros)):
    if numeros[i]==min(numeros):
        print(i, end=" - ")
print(" ")
#Crear un Lista de tamaño 10 que almacene nombres de personas
while True:
    print("""
                    MENU
    =======================================
    1) Agregar persona
    2) Eliminar persona
    """)
    seleccion=int(input("Seleccione : "))
    match seleccion:
        case 1:
            pass
        case 2:
            pass
        case _:
            pass
