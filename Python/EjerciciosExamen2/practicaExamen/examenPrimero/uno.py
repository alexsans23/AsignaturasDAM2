#1. Generar 5 numeros aleatorios y pares entre 1 y el numero
# que introduzca el usuario por consola, no se pueden repetir
# los numeros generados.

import random

numero = int(input("Escribe un número:"))

while(numero < 10):
    print("Error tu número es inferior a 10.")
    numero = int(input("Escribe un número:"))


lista = []
while len(lista) < 5:
    num = random.randint(1, numero)
    if lista.__contains__(num) or num % 2 != 0:
        continue
    else:
        lista.append(num)


print("5 números pares aleatorios y diferentes comprendidos entre el 1 y el " , numero, ":")
for numerito in lista:
    print(numerito)


####FORMA IDEAAAAAAAAAAAAAAAAL

#if num in lista:
