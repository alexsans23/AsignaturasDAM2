"""
Ejercicios genéricos de programación 1
Cada ejercicio va precedido por su enunciado (tal y como se ha pedido).
Al final hay un pequeño menú interactivo para ejecutar el ejercicio que quieras (introduce el número del ejercicio y sigue las instrucciones).
"""

import random
import math
import sys

# 1. Escribir un programa donde se muestren los 10 primeros números enteros
def ejercicio_1():
    for i in range(1, 11):
        print(i)

# 2. Escribir un programa donde se muestren los 50 primeros números pares
def ejercicio_2():
    for i in range(1, 51):
        print(2 * i)

# 3. Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado por
# el usuario (se introducirá por teclado)
def ejercicio_3():
    n = int(input("Introduce un entero (base para múltiplos): "))
    for i in range(1, 6):
        print(n * i)

# 4. Escribir un programa donde se muestren todos los números divisibles por 7 menores a
# 10000
def ejercicio_4():
    for i in range(7, 10000, 7):
        print(i)

# 5. Escribir un programa que pida por teclado un número al usuario y diga si es par o impar
def ejercicio_5():
    n = int(input("Introduce un número entero: "))
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")

# 6. Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o
# no.
def ejercicio_6():
    n = int(input("Introduce un número entero: "))
    if n % 3 == 0:
        print(f"{n} es divisible por 3")
    else:
        print(f"{n} no es divisible por 3")

# 7. Escribir un programa que pida un número por teclado al usuario que simule ser el precio de
# un artículo y escriba el resultado de aplicarle el IVA del 21%
def ejercicio_7():
    precio = float(input("Introduce el precio del artículo (euros): "))
    total = precio * 1.21
    print(f"Precio sin IVA: {precio:.2f} €")
    print(f"Precio con IVA 21%: {total:.2f} €")

# 8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
# (puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
# número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
# intereses de ningún tipo y redondeamos a dos decimales.
def ejercicio_8():
    importe = float(input("Introduce el importe total (euros): "))
    meses = int(input("Introduce el número de meses (entero): "))
    if meses <= 0:
        print("El número de meses debe ser un entero positivo.")
        return
    pago_mensual = round(importe / meses, 2)
    print(f"Pago mensual: {pago_mensual:.2f} €")

# 9. Escribir un programa que genere un número aleatorio entre el 0 y el 50 y lo muestre
def ejercicio_9():
    n = random.randint(0, 50)
    print(n)

# 10. Escribir un programa que genere dos números aleatorios simultáneamente entre el 1 y el 6
# (simulando una tirada de dos dados)
def ejercicio_10():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print(f"Dado 1: {d1}, Dado 2: {d2}")

# 11. Modificar el programa anterior para que tu programa tire dos dados de forma continuada
# hasta que el número que salga en ambos sea el mismo. En ese momento debería de parar la
# ejecución e informarnos de cuantas tiradas ha tenido que hacer para llegar a ese resultado
def ejercicio_11():
    contador = 0
    while True:
        contador += 1
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        # print(f"Tirada {contador}: {d1}, {d2}")  # opcional
        if d1 == d2:
            print(f"Se han necesitado {contador} tiradas para obtener dados iguales ({d1}, {d2}).")
            break

# 12. Escribir un programa que sirva como asistente para un juego de rol. Tu programa debería de
# pedir por teclado el número de dados que se van a tirar y el número de caras de estos (4, 6,
# 8, 12, etc.) A continuación debería de hacer la tirada y mostrarla.
def ejercicio_12():
    n_dados = int(input("Número de dados a tirar: "))
    caras = int(input("Número de caras por dado (ej. 4,6,8,12...): "))
    tiradas = [random.randint(1, caras) for _ in range(n_dados)]
    print("Resultado de la tirada:", " ".join(str(x) for x in tiradas))

# 13. Modifica el programa anterior para que no admita dados con un número de caras impares
# (¡no existen!). En el caso de meter un número impar de caras el programa debería de
# informarnos de que es erróneo y volver a preguntarnos por este dato.
def ejercicio_13():
    n_dados = int(input("Número de dados a tirar: "))
    while True:
        caras = int(input("Número de caras por dado (solo pares, ej. 4,6,8,12...): "))
        if caras % 2 == 1:
            print("Número de caras inválido: no se admiten números impares. Intenta de nuevo.")
        else:
            break
    tiradas = [random.randint(1, caras) for _ in range(n_dados)]
    print("Resultado de la tirada:", " ".join(str(x) for x in tiradas))

# 14. Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
# comprendido entre ambos. Por el momento no te preocupes de que el primer número
# siempre debería de ser menor que el segundo, simplemente no los metas en un orden
# incorrecto.
def ejercicio_14():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    n = random.randint(a, b)
    print(n)

# 15. Modificar el programa del punto anterior para que si el primer número que metemos es
# mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el 50 y
# en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y no entre el
# 50 y el 10 que no tiene mucha lógica…)
def ejercicio_15():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    low, high = min(a, b), max(a, b)
    n = random.randint(low, high)
    print(n)

# 16. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando una
# lotería primitiva). Por el momento no te preocupes de que algunos números puedan salir
# repetidos. Ya resolveremos eso más adelante.
def ejercicio_16():
    numeros = [random.randint(1, 49) for _ in range(6)]
    print("Números generados:", " ".join(str(x) for x in numeros))

# 17. Escribir un programa que nos permita generar una quiniela. Para ello nos debe generar
# quince números aleatorios entre el 1 y el 3. Recuerda que los resultados válidos son 1 X o 2,
# así que si te sale un 3 lo que tienes que imprimir en pantalla es una X
def ejercicio_17():
    resultados = []
    for _ in range(15):
        v = random.randint(1, 3)
        if v == 3:
            resultados.append('X')
        else:
            resultados.append(str(v))
    print("Quiniela:")
    for i, r in enumerate(resultados, 1):
        print(f"{i}: {r}")

# 18. Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que sólo
# se detenga cuando salga el 666. Los números que ha tenido que generar tu programa hasta
# aparecer el 666 son los que restan para el apocalipsis. Tu programa debería de indicarlo con
# un mensaje tétrico (¡Faltan 236 días para que se acabe todo! por ejemplo)
def ejercicio_18():
    contador = 0
    while True:
        contador += 1
        v = random.randint(1, 1000)
        if v == 666:
            print(f"¡Faltan {contador} días para que se acabe todo!")
            break

# 19. Escribir un programa que pida un número por teclado y nos muestre sus divisores
def ejercicio_19():
    n = int(input("Introduce un número entero positivo: "))
    if n <= 0:
        print("Introduce un entero positivo.")
        return
    divisores = [i for i in range(1, n + 1) if n % i == 0]
    print("Divisores:", " ".join(str(d) for d in divisores))

# 20. Escribir un programa que nos pida tres números por teclado en cualquier orden y nos los
# muestre en pantalla ordenados de menor a mayor
def ejercicio_20():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    c = float(input("Introduce el tercer número: "))
    lista = sorted([a, b, c])
    print("Menor a mayor:", " ".join(str(x) for x in lista))

# 21. Escribir un programa que pida por teclado un número al usuario y calcule si es primo o no
def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def ejercicio_21():
    n = int(input("Introduce un número entero: "))
    if es_primo(n):
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")

# 22. Escribir un programa que genere un número primo aleatorio entre el 10.000.000 y el
# 50.000.000
def ejercicio_22(max_tries=1000000):
    low, high = 10_000_000, 50_000_000
    tries = 0
    while True:
        if tries >= max_tries:
            print("No se ha encontrado un primo en el número máximo de intentos. Intenta de nuevo")
            return
        n = random.randint(low, high)
        if es_primo(n):
            print(f"Primo encontrado: {n}")
            return
        tries += 1

# 23. Escribir un programa que te escriba todos los números primos que hay entre el 1 y el 100
def ejercicio_23():
    primos = [n for n in range(1, 101) if es_primo(n)]
    print("Primos entre 1 y 100:", ", ".join(str(p) for p in primos))

# 24. Modifica el programa anterior para que sea el usuario quién introduzca dos números y se nos
# muestre los primos que hay entre ambos
def ejercicio_24():
    a = int(input("Introduce límite inferior: "))
    b = int(input("Introduce límite superior: "))
    low, high = min(a, b), max(a, b)
    primos = [n for n in range(low, high + 1) if es_primo(n)]
    print(f"Primos entre {low} y {high}:")
    if primos:
        print(", ".join(str(p) for p in primos))
    else:
        print("No hay primos en ese rango.")

# 25. Escribir un programa que reciba por teclado un número y muestre sucesivamente el
# resultado de ir dividiéndolo por dos sucesivamente hasta llegar a un número igual o menor a
# 1. Caso de ser necesario los resultados se mostrarán con dos decimales.
def ejercicio_25():
    n = float(input("Introduce un número (se irá dividiendo entre 2 hasta <=1): "))
    print(f"Has introducido el número {int(n) if n.is_integer() else n}")
    current = n
    while True:
        current = current / 2
        # Si el número es entero lo mostramos sin decimales, si no con 2 decimales
        if abs(current - round(current)) < 1e-9:
            print(int(round(current)))
        else:
            print(f"{current:.2f}")
        if current <= 1:
            break


# Menú simple para ejecutar ejercicios
ejercicios = {i: globals()[f"ejercicio_{i}"] for i in range(1, 26)}

def menu():
    print("Ejercicios genéricos de programación 1 - menú")
    print("Introduce el número del ejercicio que quieras ejecutar (1-25) o 0 para salir.")
    while True:
        try:
            opcion = int(input("Ejercicio (0 para salir): "))
        except ValueError:
            print("Introduce un entero válido.")
            continue
        if opcion == 0:
            print("Saliendo. Hasta luego!")
            break
        funcion = ejercicios.get(opcion)
        if funcion:
            print(f"--- Ejecutando ejercicio {opcion} ---")
            try:
                funcion()
            except Exception as e:
                print(f"Error durante la ejecución: {e}")
            print(f"--- Fin ejercicio {opcion} ---")
        else:
            print("Opción no válida. Elige un número entre 1 y 25 o 0 para salir.")


if __name__ == '__main__':
    menu()
