# 3. Igual que el anterior pero con dado trucado: el 6 tiene 3 veces más probabilidad que cualquier otro número.
#    Mostrar tiradas, porcentajes (dos decimales) y número de tiradas hasta que todos sean iguales.

import random

n = int(input("Número de dados: "))
veces = 0
cuentas = [0,0,0,0,0,0,0]  # índices 1..6
total_resultados = 0

# población y pesos (1..6), con 6 con peso 3
poblacion = [1,2,3,4,5,6]
pesos =     [1,1,1,1,1,3]

while True:
    # generar una tirada de n dados con probabilidad sesgada
    tirada = random.choices(poblacion, weights=pesos, k=n)
    veces += 1
    print(" - ".join(str(x) for x in tirada))
    for x in tirada:
        cuentas[x] += 1
        total_resultados += 1
    if len(set(tirada)) == 1:
        break

for num in range(1,7):
    porcentaje = cuentas[num] / total_resultados * 100
    print(f"El número {num} ha salido el {porcentaje:.2f} % de las veces")

print(f"He tenido que tirar los dados {veces} veces para que salgan todos iguales")
