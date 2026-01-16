#Generar 10 numeros aleatorios entre 1 y 1000,
# mostrarlos y decir cuantos pares e impares hay , y decir el mayor y el menor.
import random


contPares = 0
contImpares = 0
lista = []

for i in range (1, 11):
    num = random.randint(1, 1000)
    if num % 2 == 0:
        contPares+= 1
    else:
        contImpares+=1
    lista.append(num)


print("10 números entre el 1 y el 1000")

print(lista[0], ", " ,lista[1], ", " ,lista[2], ", " ,lista[3], ", " ,lista[4], ", " ,lista[5], ", " ,lista[6], ", ", lista[7], ", ",lista[8], ", ",lista[9])
print(", ".join(str(n) for n in lista))
print(str(lista)[1:-1])  # Esto imprime: 130, 823, 903, ...
print("He generado ", contPares, " números pares y ", contImpares, " impares")
print("El número mayor ha sido el ", max(lista), " y el menor el ", min(lista))