"""
Ejercicios genéricos de programación 2
Cada ejercicio está precedido por su enunciado tal y como lo enviaste.
Al final hay un menú simple para ejecutar cualquier ejercicio.

Nota ejercicio 18: Para calcular las retenciones he usado una tabla de tramos del IRPF
(combinando tipos a nivel nacional/autonómico en una escala marginal) para el año 2022.
Los tramos usados son:
0 - 12_450 : 19%
12_450 - 20_200 : 24%
20_200 - 35_200 : 30%
35_200 - 60_000 : 37%
60_000 - 300_000 : 45%
>300_000 : 47%

(He incluido la implementación usando esos tramos; si quieres que use la escala estatal+autonómica
por separado o que busque los tramos exactos de una comunidad autónoma, dímelo.)
"""

import random
import math

# 1. Escribir un programa que nos pida tres palabras por teclado en cualquier orden y nos
# las muestre en pantalla ordenadas alfabeticamente en orden ascendente
def ejercicio_1():
    a = input("Introduce la primera palabra: ")
    b = input("Introduce la segunda palabra: ")
    c = input("Introduce la tercera palabra: ")
    lista = sorted([a, b, c])
    print("Orden ascendente:", ", ".join(lista))

# 2. Idem al anterior pero ordenando ahora en orden descendente
def ejercicio_2():
    a = input("Introduce la primera palabra: ")
    b = input("Introduce la segunda palabra: ")
    c = input("Introduce la tercera palabra: ")
    lista = sorted([a, b, c], reverse=True)
    print("Orden descendente:", ", ".join(lista))

# 3. Escribir un programa que pida un número por teclado al usuario que simule ser el
# precio de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado
# debe de estar redondeado a dos decimales.
def ejercicio_3():
    precio = float(input("Introduce el precio del artículo (euros): "))
    total = round(precio * 1.21, 2)
    print(f"Precio con IVA (21%): {total:.2f} €")

# 4. Escribir un programa que nos pida por teclado dos calificaciones numéricas de un
# alumno y nos muestre la media aritmética resultante redondeada sin decimales. Las
# notas introducidas deben de estar entre 0 y 10 y admiten decimales. Caso de que una
# entrada sea errónea debería de advertirnos de ello y no hacer el cálculo
def ejercicio_4():
    try:
        n1 = float(input("Introduce la primera nota (0-10): "))
        n2 = float(input("Introduce la segunda nota (0-10): "))
    except ValueError:
        print("Entrada inválida: introduce números.")
        return
    if not (0 <= n1 <= 10) or not (0 <= n2 <= 10):
        print("Las notas deben estar entre 0 y 10.")
        return
    media = (n1 + n2) / 2
    print(f"Media redondeada sin decimales: {round(media):.0f}")

# 5. Escribir un programa que nos pida las notas obtenidas en un trimestre y nos muestre
# la media ponderada sabiendo que;
# 1. La primera nota corresponde al trabajo en clase y cuenta como un 5% del total
# 2. La segunda corresponde a los ejercicios prácticos: 15%
# 3. La tercera la nota del examen: 80%
# El resultado debería de mostrarse de dos formas: redondeado con dos decimales
# (nota real) y sin redondeada sin decimales (nota de boletín).
def ejercicio_5():
    try:
        t = float(input("Nota trabajo en clase (0-10): "))
        p = float(input("Nota ejercicios prácticos (0-10): "))
        e = float(input("Nota examen (0-10): "))
    except ValueError:
        print("Entrada inválida: introduce números.")
        return
    for val in (t, p, e):
        if not (0 <= val <= 10):
            print("Todas las notas deben estar entre 0 y 10.")
            return
    nota_real = t * 0.05 + p * 0.15 + e * 0.80
    print(f"Nota real (2 decimales): {nota_real:.2f}")
    print(f"Nota de boletín (sin decimales): {int(round(nota_real))}")

# 6. Modifica el ejercicio anterior para que la nota del boletín se redondee
# matemáticamente si es superior a 5 pero se trunquen los decimales si es inferior a 5
def ejercicio_6():
    try:
        t = float(input("Nota trabajo en clase (0-10): "))
        p = float(input("Nota ejercicios prácticos (0-10): "))
        e = float(input("Nota examen (0-10): "))
    except ValueError:
        print("Entrada inválida: introduce números.")
        return
    for val in (t, p, e):
        if not (0 <= val <= 10):
            print("Todas las notas deben estar entre 0 y 10.")
            return
    nota_real = t * 0.05 + p * 0.15 + e * 0.80
    print(f"Nota real (2 decimales): {nota_real:.2f}")
    if nota_real > 5:
        boletin = int(round(nota_real))
    else:
        boletin = int(nota_real)  # truncar
    print(f"Nota de boletín según regla: {boletin}")

# 7. Escribir un programa que pida un número por teclado y nos imprima la tabla de
# multiplicar de dicho número del 1 al 10.
def ejercicio_7():
    n = int(input("Introduce un número entero: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# 8. Escribe un programa que pida un número por teclado y escriba todos sus divisores
# separados por comas (y evitando poner una coma al final).
def ejercicio_8():
    n = int(input("Introduce un número entero positivo: "))
    if n <= 0:
        print("Introduce un entero positivo.")
        return
    divisores = [str(i) for i in range(1, n + 1) if n % i == 0]
    print(f"Divisores del número {n}: {', '.join(divisores)}")

# 9. Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que
# escribamos la palabra FIN (con mayúsculas). Si el usuario introduce una entrada
# inválida (números superiores a 100, otras cadenas de caracteres que no sean FIN, etc.)
# no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá
# su curso. Cuando terminamos (al introducir la palabra FIN, recuerda) mostraremos
# por pantalla el numero de entradas válidas que hemos hecho (sin contar esta última
# que sólo sirve para finalizar el programa)
def ejercicio_9():
    contador = 0
    while True:
        s = input("Introduce un número entre 1 y 100 (o FIN para terminar): ")
        if s == 'FIN':
            break
        try:
            v = int(s)
        except ValueError:
            print("Entrada inválida: no es un número ni FIN.")
            continue
        if 1 <= v <= 100:
            contador += 1
        else:
            print("Número fuera de rango (1-100).")
    print(f"Entradas válidas: {contador}")

# 10. Modificar el programa anterior para que nos muestre al final la media aritmética de
# las entradas válidas
def ejercicio_10():
    valores = []
    while True:
        s = input("Introduce un número entre 1 y 100 (o FIN para terminar): ")
        if s == 'FIN':
            break
        try:
            v = int(s)
        except ValueError:
            print("Entrada inválida: no es un número ni FIN.")
            continue
        if 1 <= v <= 100:
            valores.append(v)
        else:
            print("Número fuera de rango (1-100).")
    if valores:
        media = sum(valores) / len(valores)
        print(f"Entradas válidas: {len(valores)}, media: {media:.2f}")
    else:
        print("No se introdujeron entradas válidas.")

# 11. Modificar el programa anterior para que, además, nos diga al final cual han sido el
# número mayor y el menor que has introducido
def ejercicio_11():
    valores = []
    while True:
        s = input("Introduce un número entre 1 y 100 (o FIN para terminar): ")
        if s == 'FIN':
            break
        try:
            v = int(s)
        except ValueError:
            print("Entrada inválida: no es un número ni FIN.")
            continue
        if 1 <= v <= 100:
            valores.append(v)
        else:
            print("Número fuera de rango (1-100).")
    if valores:
        media = sum(valores) / len(valores)
        print(f"Entradas válidas: {len(valores)}, media: {media:.2f}")
        print(f"Mayor: {max(valores)}, Menor: {min(valores)}")
    else:
        print("No se introdujeron entradas válidas.")

# 12. Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
# ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
# has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
# se superan el número máximo de intentos establecidos en 5.
def ejercicio_12():
    secreto = random.randint(1, 50)
    max_intentos = 5
    for intento in range(1, max_intentos + 1):
        try:
            v = int(input(f"Intento {intento}/{max_intentos}. Adivina el número (1-50): "))
        except ValueError:
            print("Introduce un número entero.")
            continue
        if v == secreto:
            print("¡Acertaste!")
            return
        elif v < secreto:
            print("Te has quedado corto.")
        else:
            print("Te has pasado.")
    print(f"Se han agotado los intentos. El número era {secreto}.")

# 13. Modifica el programa anterior para que el programa te de todos los intentos que
# necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
# lograrlo
def ejercicio_13():
    secreto = random.randint(1, 50)
    intentos = 0
    while True:
        intentos += 1
        try:
            v = int(input(f"Intento {intentos}. Adivina el número (1-50): "))
        except ValueError:
            print("Introduce un número entero.")
            continue
        if v == secreto:
            print(f"¡Acertaste! Fallaste {intentos-1} veces antes.")
            break
        elif v < secreto:
            print("Te has quedado corto.")
        else:
            print("Te has pasado.")

# 14. Modifica el programa anterior para que al final del programa te pida si quieres volver
# a jugar y en caso afirmativo comience una nueva partida
def ejercicio_14():
    while True:
        secreto = random.randint(1, 50)
        intentos = 0
        while True:
            intentos += 1
            try:
                v = int(input(f"Intento {intentos}. Adivina el número (1-50): "))
            except ValueError:
                print("Introduce un número entero.")
                continue
            if v == secreto:
                print(f"¡Acertaste! Fallaste {intentos-1} veces antes.")
                break
            elif v < secreto:
                print("Te has quedado corto.")
            else:
                print("Te has pasado.")
        r = input("¿Quieres volver a jugar? (s/n): ")
        if r.lower() != 's':
            break

# 15. Modifica el programa anterior para que al iniciar el juego te pida dos parámetros con
# objeto de cambiar la dificultad del juego: el número máximo (antes era siempre 50) o
# el número de intentos posibles (antes era siempre 5).
def ejercicio_15():
    try:
        max_num = int(input("Número máximo (ej. 50): "))
        max_intentos = int(input("Número máximo de intentos (ej. 5): "))
    except ValueError:
        print("Introduce enteros válidos.")
        return
    while True:
        secreto = random.randint(1, max_num)
        intentos = 0
        while intentos < max_intentos:
            intentos += 1
            try:
                v = int(input(f"Intento {intentos}/{max_intentos}. Adivina el número (1-{max_num}): "))
            except ValueError:
                print("Introduce un número entero.")
                continue
            if v == secreto:
                print(f"¡Acertaste! Fallaste {intentos-1} veces antes.")
                break
            elif v < secreto:
                print("Te has quedado corto.")
            else:
                print("Te has pasado.")
        else:
            print(f"Se han agotado los intentos. El número era {secreto}.")
        r = input("¿Quieres volver a jugar? (s/n): ")
        if r.lower() != 's':
            break

# 16. Escribe un programa que pida por teclado el radio de una circunferencia, admitiendo
# valores con decimales y calcule la longitud y el área de la circunferencia (redondeando
# a cinco decimales). Si no las recuerdas, las fórmulas son las siguientes:
# area = 3.14159 * radio2
# longitud = 2 * 3.14159 * radio
def ejercicio_16():
    r = float(input("Introduce el radio de la circunferencia: "))
    area = 3.14159 * r * r
    longitud = 2 * 3.14159 * r
    print(f"Área: {area:.5f}")
    print(f"Longitud: {longitud:.5f}")

# 17. Escribir un programa que reciba por teclado una temperatura en cualquiera de las
# tres unidades básicas (Celcius, Farenheit o Kelvin) y la devuelva en las otras dos.
# Tu programa reconocerá la unidad que has usado al introducir la entrada por teclado
# porque irá acompañado de una letra que lo indique. Por ejemplo, 12C, 280.57K o
# 98.6F
# Se admitirán decimales en la entrada, y se devolverá el resultado con dos decimales

def ejercicio_17():
    s = input("Introduce la temperatura seguida de la unidad (ej. 12C, 98.6F, 280.57K): ")
    if len(s) < 2:
        print("Entrada inválida.")
        return
    unit = s[-1].upper()
    try:
        val = float(s[:-1])
    except ValueError:
        print("Valor numérico inválido.")
        return
    if unit == 'C':
        f = val * 1.8 + 32
        k = val + 273.15
        print(f"{val:.2f}C = {f:.2f}F = {k:.2f}K")
    elif unit == 'F':
        c = (val - 32) / 1.8
        k = (val - 32) * 5/9 + 273.15
        print(f"{val:.2f}F = {c:.2f}C = {k:.2f}K")
    elif unit == 'K':
        c = val - 273.15
        f = 1.8 * (val - 273.15) + 32
        print(f"{val:.2f}K = {c:.2f}C = {f:.2f}F")
    else:
        print("Unidad no reconocida. Usa C, F o K.")

# 18. La tabla de tarifas impositivas en España para 2022 es la siguiente: (buscalo en internet los tramos y ya
# Escribe un programa que le pida al usuario su sueldo anual (lógicamente puede ser
# un número con decimales) y le informe que porcentaje de retención le corresponde, el
# importe de la misma y el importe neto restante que cobrará.
# Implementación: usamos una escala marginal de tramos generales (combinada) para 2022.

def ejercicio_18():
    tramos = [
        (0, 12450, 0.19),
        (12450, 20200, 0.24),
        (20200, 35200, 0.30),
        (35200, 60000, 0.37),
        (60000, 300000, 0.45),
        (300000, float('inf'), 0.47),
    ]
    sueldo = float(input("Introduce tu sueldo anual bruto (euros): "))
    impuesto = 0.0
    restante = sueldo
    for low, high, tipo in tramos:
        if sueldo > low:
            aplicable = min(sueldo, high) - low
            impuesto += aplicable * tipo
    porcentaje_efectivo = (impuesto / sueldo * 100) if sueldo > 0 else 0
    neto = sueldo - impuesto
    # marginal: buscar el tramo donde queda el sueldo
    marginal = next(tipo for low, high, tipo in tramos if low <= sueldo <= high if True) if sueldo >= 0 else None
    print(f"Sueldo bruto: {sueldo:.2f} €")
    print(f"Impuesto total: {impuesto:.2f} €")
    print(f"Porcentaje efectivo retenido: {porcentaje_efectivo:.2f}%")
    if marginal is not None:
        print(f"Tipo marginal (tramo en el que estás): {marginal*100:.2f}%")
    print(f"Sueldo neto aproximado: {neto:.2f} €")


# Menú

ejercicios = {i: globals()[f"ejercicio_{i}"] for i in range(1, 19)}

def menu():
    print("Ejercicios genéricos de programación 2 - menú")
    print("Introduce el número del ejercicio que quieras ejecutar (1-18) o 0 para salir.")
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
            print("Opción no válida. Elige un número entre 1 y 18 o 0 para salir.")


if __name__ == '__main__':
    menu()
