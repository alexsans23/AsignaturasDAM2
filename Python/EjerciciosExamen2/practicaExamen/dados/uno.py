# 1. Escribir un programa que genere tiradas de n dados (1-6) hasta que todos sean iguales.
#    Pedir por teclado el número de dados. Mostrar cada tirada y al final cuántas tiradas hizo.

import random

n = int(input("Número de dados: "))
veces = 0

while True:
    tirada = [random.randint(1,6) for _ in range(n)]
    veces += 1
    print(" - ".join(str(x) for x in tirada))
    if len(set(tirada)) == 1:
        break

print(f"He tenido que tirar los dados {veces} veces para que salgan todos iguales")
