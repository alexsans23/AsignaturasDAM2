"""
Ejercicios genéricos de programación 5
Cada ejercicio va precedido por su enunciado (tal y como lo pediste).
Al final hay un pequeño menú interactivo para ejecutar el ejercicio que quieras (1-6).
"""

import random
import re
from collections import Counter

# 1. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
# ninguno de ellos esté repetido (simulando una lotería primitiva).
def ejercicio_1():
    numeros = random.sample(range(1, 50), 6)  # sample asegura unicidad
    print("Números generados (orden aleatorio):", ' '.join(str(n) for n in numeros))
    print("Números ordenados:", ' '.join(str(n) for n in sorted(numeros)))

# 2. Hacer un programa en que nos permita calcular todos los divisores comunes a dos
# números
def ejercicio_2():
    try:
        a = int(input("Introduce el primer entero positivo: "))
        b = int(input("Introduce el segundo entero positivo: "))
    except ValueError:
        print("Entrada inválida: introduce enteros.")
        return
    if a <= 0 or b <= 0:
        print("Introduce enteros positivos.")
        return
    def divisores(n):
        ds = set()
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                ds.add(i)
                ds.add(n // i)
        return ds
    comunes = sorted(divisores(a).intersection(divisores(b)))
    if comunes:
        print(f"Divisores comunes de {a} y {b}: {', '.join(str(x) for x in comunes)}")
    else:
        print("No tienen divisores comunes (aparte del 1, que debería aparecer en caso de serlo).")

# 3. Escribir un programa que cuenta las palabras que tiene una frase introducida
# previamente por teclado. Las palabras pueden estar separadas por más de un espacio
# pero siempre debe de haber al menos uno. No tenemos en cuenta los signos de
# puntuación como separadores.
def ejercicio_3():
    s = input("Introduce una frase: ")
    # split() separa por cualquier cantidad de espacios en blanco
    palabras = [w for w in s.split() if w != '']
    print(f"Número de palabras: {len(palabras)}")

# 4. Escribir un programa que nos pida una cadena por teclado y luego cuente cuantas
# palabras hay en ella con cuatro o más vocales diferentes. (Vocales: a,e,i,o,u ; sin tildes)
def ejercicio_4():
    s = input("Introduce una frase: ")
    palabras = [w for w in s.split() if w != '']
    vocales = set('aeiouAEIOU')
    contador = 0
    for w in palabras:
        # extraer solo letras para evitar signos de puntuación pegados
        partes = re.findall(r"[A-Za-z]+", w)
        if not partes:
            continue
        palabra_limpia = ''.join(partes)
        presentes = set(ch.lower() for ch in palabra_limpia if ch in vocales)
        if len(presentes) >= 4:
            contador += 1
    print(f"Palabras con cuatro o más vocales diferentes: {contador}")

# 5. Escribe un programa que genere 100 números aleatorios comprendidos entre el 1 y
# 50 (ambos inclusive) y, posteriormente, obtenga el mayor, el menor y el que mas veces
# se repite (y nos diga cuantas veces lo hace).
def ejercicio_5():
    numeros = [random.randint(1, 50) for _ in range(100)]
    mayor = max(numeros)
    menor = min(numeros)
    conteo = Counter(numeros)
    mas_comun, veces = conteo.most_common(1)[0]
    print(f"Números generados: {', '.join(str(n) for n in numeros)}")
    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")
    print(f"Número que más se repite: {mas_comun} (aparece {veces} veces)")

# 6. Escribe un programa que nos permita contar el número de veces que se repite cada
# cifra en un número. Por ejemplo, el número 885210003 tiene tres 0, un 1, un 2, un 5 y
# dos 8.
def ejercicio_6():
    s = input("Introduce un número (puedes incluir signo): ")
    # quedarnos sólo con los dígitos
    digitos = ''.join(ch for ch in s if ch.isdigit())
    if not digitos:
        print("No se han encontrado dígitos en la entrada.")
        return
    conteo = Counter(digitos)
    print("Recuento de cifras:")
    for d in sorted(conteo.keys()):
        print(f"Dígito {d}: {conteo[d]} vez/veces")


# Menú

ejercicios = {i: globals()[f"ejercicio_{i}"] for i in range(1, 7)}

def menu():
    print("Ejercicios genéricos de programación 5 - menú")
    print("Introduce el número del ejercicio que quieras ejecutar (1-6) o 0 para salir.")
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
            print("Opción no válida. Elige un número entre 1 y 6 o 0 para salir.")


if __name__ == '__main__':
    menu()
