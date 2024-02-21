"Crear un programa que genere una lista de números aleatorios y los imprima en pantalla"
import random
lista=[]
for i in range(5):
    aleatorio= random.randint(1,20)
    n= lista.append(aleatorio)
print(lista)