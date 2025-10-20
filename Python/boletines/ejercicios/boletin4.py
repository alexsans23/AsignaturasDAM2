"""
Ejercicios genéricos de programación 4
Cada ejercicio aparece precedido por su enunciado (tal y como pediste).
Al final hay un menú interactivo para ejecutar los ejercicios (1-14).
"""

import math

# 1. Escribir un programa que pida un número por teclado y calcule su factorial.
# Por ejemplo, 6! = 6*5*4*3*2*1 = 720
def ejercicio_1():
    n = int(input("Introduce un entero no negativo para calcular su factorial: "))
    if n < 0:
        print("El factorial no está definido para números negativos.")
        return
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"{n}! = {fact}")

# 2. Programa que reciba un número por teclado y calcule tantos números de la
# sucesión de fibonacci como indique ese número (terminología: n términos).
def ejercicio_2():
    n = int(input("¿Cuántos términos de la sucesión de Fibonacci quieres? "))
    if n <= 0:
        print("Introduce un entero positivo.")
        return
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    print(','.join(str(x) for x in fib))

# 3. Programa que reciba un número por teclado y muestre todos los números de la
# sucesión de Fibonacci que sean menores o iguales al número introducido.
def ejercicio_3():
    limite = int(input("Introduce el límite (mostrar Fibonacci <= límite): "))
    if limite < 0:
        print("Límite negativo: no hay términos de Fibonacci negativos en esta definición.")
        return
    a, b = 0, 1
    salida = []
    while a <= limite:
        salida.append(a)
        a, b = b, a + b
    print(','.join(str(x) for x in salida))

# 4. Escribir un programa que cuente el número de cifras que tiene un número.
# Ej: 8 -> 1, 221 -> 3, 456789 -> 6
def ejercicio_4():
    s = input("Introduce un número entero: ")
    s = s.strip()
    if s.startswith('-'):
        s = s[1:]
    if not s.isdigit():
        print("Entrada inválida: introduce un entero.")
        return
    # '0' tiene 1 cifra
    print(f"El número tiene {len(s)} cifra(s).")

# 5. Escribir un programa que nos diga si un número es capicúa (palíndromo numérico).
def ejercicio_5():
    s = input("Introduce un número: ")
    s = s.strip()
    negativo = s.startswith('-')
    if negativo:
        s = s[1:]
    if not s.isdigit():
        print("Entrada inválida: introduce un número.")
        return
    if s == s[::-1]:
        print("El número es capicúa.")
    else:
        print("El número NO es capicúa.")

# 6. Mostrar por pantalla los 50 primeros números primos, sus raíces cuadradas,
# sus cuadrados y sus cubos.
def _es_primo(n: int) -> bool:
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

def ejercicio_6():
    primos = []
    n = 2
    while len(primos) < 50:
        if _es_primo(n):
            primos.append(n)
        n += 1
    print("Primo | sqrt(primo) | cuadrado | cubo")
    for p in primos:
        print(f"{p:5d} | {math.sqrt(p):10.5f} | {p*p:8d} | {p**3:12d}")

# 7. Calcular la primera pareja de primos gemelos por encima del 50.
def ejercicio_7():
    n = 51
    prev_primo = None
    while True:
        if _es_primo(n):
            if prev_primo is not None and n - prev_primo == 2:
                print(f"Primera pareja de primos gemelos por encima de 50: {prev_primo} y {n}")
                return
            prev_primo = n
        n += 1

# 8. Sumar las cifras pares por un lado y las impares por otro y mostrar ambos resultados.
# Ejemplo: 128 -> pares: 8+0? actually digits 1,2,8 -> pares 2+8=10 impares 1
def ejercicio_8():
    s = input("Introduce un número entero: ")
    s = s.strip()
    if s.startswith('-'):
        s = s[1:]
    if not s.isdigit():
        print("Entrada inválida")
        return
    suma_pares = 0
    suma_impares = 0
    for ch in s:
        d = int(ch)
        if d % 2 == 0:
            suma_pares += d
        else:
            suma_impares += d
    print(f"Suma cifras pares: {suma_pares}")
    print(f"Suma cifras impares: {suma_impares}")

# 9. Pedir una cadena y un carácter; imprimir cuántas veces aparece y las posiciones (0-indexadas).
def ejercicio_9():
    s = input("Introduce una cadena: ")
    c = input("Introduce un carácter a buscar: ")
    if len(c) != 1:
        print("Introduce exactamente un carácter.")
        return
    posiciones = [i for i, ch in enumerate(s) if ch == c]
    print(f"La '{c}' aparece en {len(posiciones)} ocasión(es)")
    if posiciones:
        print("Las posiciones en las que aparece son:", ','.join(str(p) for p in posiciones))

# 10. Pedir una cadena y devolver sólo las cifras que aparecen en ella concatenadas.
def ejercicio_10():
    s = input("Introduce una cadena: ")
    cifras = ''.join(ch for ch in s if ch.isdigit())
    print(cifras)

# 11. Pedir una frase e imprimir separando los caracteres de cada palabra con un guión
# ejemplo: "esto es una prueba" -> "e-s-t-o e-s u-n-a p-r-u-e-b-a"
def ejercicio_11():
    frase = input("Introduce una frase: ")
    palabras = frase.split(' ')
    partes = []
    for palabra in palabras:
        if palabra == '':
            partes.append('')
        else:
            partes.append('-'.join(list(palabra)))
    print(' '.join(partes))

# 12. Indicar si un año es bisiesto usando la regla completa (divisible por 4, no por 100 salvo si por 400).
def ejercicio_12():
    anyo = int(input("Introduce un año (entero): "))
    es = (anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0))
    print(f"Año {anyo} bisiesto: {'Sí' if es else 'No'}")

# 13. Leer un número y un carácter y visualizar una matriz n x n repitiendo ese carácter.
def ejercicio_13():
    n = int(input("Introduce el tamaño de la matriz (entero positivo): "))
    ch = input("Introduce el carácter a usar: ")
    if n <= 0:
        print("El tamaño debe ser positivo.")
        return
    if len(ch) == 0:
        print("Introduce un carácter válido.")
        return
    c = ch[0]
    for _ in range(n):
        print(c * n)

# 14. Leer una hora en formato 24h HH:MM y decir si corresponde a mañana/tarde/noche/madrugada
# También validar formato y rangos.
def ejercicio_14():
    s = input("Introduce una hora en formato HH:MM: ")
    s = s.strip()
    if not s or ':' not in s:
        print("Formato inválido")
        return
    partes = s.split(':')
    if len(partes) != 2:
        print("Formato inválido")
        return
    hh_s, mm_s = partes[0], partes[1]
    if not (hh_s.isdigit() and mm_s.isdigit()):
        print("Formato inválido: horas y minutos deben ser números.")
        return
    hh, mm = int(hh_s), int(mm_s)
    if not (0 <= hh <= 23 and 0 <= mm <= 59):
        print("Hora no válida.")
        return
    if 6 <= hh <= 11:
        parte = 'mañana'
    elif 12 <= hh <= 19:
        parte = 'tarde'
    elif 20 <= hh <= 23:
        parte = 'noche'
    else:  # 0-5
        parte = 'madrugada'
    print(f"La hora {s} corresponde a la {parte}.")


# Menú para ejecutar ejercicios

ejercicios = {i: globals()[f"ejercicio_{i}"] for i in range(1, 15)}

def menu():
    print("Ejercicios genéricos de programación 4 - menú")
    print("Introduce el número del ejercicio que quieras ejecutar (1-14) o 0 para salir.")
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
            print("Opción no válida. Elige un número entre 1 y 14 o 0 para salir.")


if __name__ == '__main__':
    menu()
