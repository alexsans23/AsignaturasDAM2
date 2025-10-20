"""
1. Escribir un programa que genere de forma consecutiva tiradas de dados aleatorios entre
   el 1 y el 6 ambos incluidos y los muestre en pantalla finalizando la ejecución cuando
   el valor de todos los dados sea el mismo. El número de dados se pedirá por teclado.
   Al finalizar debe de devolver el número de veces que ha tenido que lanzar los dados
   para alcanzar ese valor.

Salida de ejemplo (tres dados):
2 - 5 - 1
4 - 1 - 4
4 - 6 - 6
3 - 3 - 3
He tenido que lanzar los dados 4 veces para que todos sean iguales
"""
import random

dado1 = 0
dado2 = 1
contador = 0

while dado1 != dado2:
    contador += 1
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    print(dado1, "-", dado2)

print("He tenido que lanzar los dados", contador, "veces para que todos sean iguales")

"""
2. Modifica la función anterior para que nos muestre estadísticas del porcentaje de veces que
   ha salido cada dado. El porcentaje de aparición saldrá con dos decimales.

Nota: el porcentaje se calcula sobre el total de caras mostradas (número_de_tiradas * número_de_dados).
Salida de ejemplo (parcial):
5 - 3 - 1
5 - 6 - 2
6 - 6 - 4
...
El número 1 ha salido el 21.14 % de las veces
...
He tenido que tirar los dados 41 veces para que salgan todos iguales
"""

# dos.py
import random
from collections import Counter
import random

dado1 = 0
dado2 = 1
lanzamientos = 0
contadores = [0] * 7  # usaremos índices 1..6

while dado1 != dado2:
    lanzamientos += 1
    dado1 = random.randint(1, 6); contadores[dado1] += 1
    dado2 = random.randint(1, 6); contadores[dado2] += 1
    print(dado1, "-", dado2)

for cara in range(1, 7):
    print("Cara", cara, ":", contadores[cara] / (lanzamientos*2) * 100 , "%")

print("He tenido que lanzar los dados", lanzamientos, "veces para que todos sean iguales")


"""
3. Modifica de nuevo tu código para que el dado esté trucado y el número 6 tenga tres veces
   más probabilidades de aparecer que cualquier otro número.

Implementación: se usan probabilidades con pesos: caras 1..5 peso 1 cada una; cara 6 peso 3.
Ejemplo de salida (parcial):
3 - 6 - 6
1 - 6 - 6
...
El número 1 ha salido el  4.76 % de las veces
...
El número 6 ha salido el 57.14 % de las veces
He tenido que tirar los dados 7 veces para que salgan todos iguales
"""
import random

# Lista con 6 repetido 3 veces → el 6 tiene tres veces más probabilidad
caras = [1, 2, 3, 4, 5, 6, 6, 6]

dado1 = 0
dado2 = 1
lanzamientos = 0
contadores = [0] * 7  # índices 1..6

while dado1 != dado2:
    lanzamientos += 1
    dado1 = random.choice(caras); contadores[dado1] += 1
    dado2 = random.choice(caras); contadores[dado2] += 1
    print(dado1, "-", dado2)

for cara in range(1, 7):
    print("Cara", cara, ":", contadores[cara] / (lanzamientos * 2) * 100, "%")

print("He tenido que lanzar los dados", lanzamientos, "veces para que todos sean iguales")
