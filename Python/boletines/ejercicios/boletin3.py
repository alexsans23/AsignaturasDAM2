"""
Ejercicios genéricos de programación 3
Cada ejercicio va precedido por su enunciado tal como lo enviaste.
Al final hay un menú para ejecutar cualquiera de los ejercicios (1-15).
"""

import re

# 1. Escribir un programa que pida una contraseña por teclado (dos veces) y si no
# coinciden nos lo vuelva a pedir hasta que lo hagan
def ejercicio_1():
    while True:
        p1 = input("Introduce la contraseña: ")
        p2 = input("Vuelve a introducir la contraseña: ")
        if p1 == p2:
            print("Contraseñas coinciden.")
            return
        print("No coinciden. Inténtalo de nuevo.")

# 2. Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
# informe del número de intentos inválidos
def ejercicio_2():
    intentos_invalidos = 0
    while True:
        p1 = input("Introduce la contraseña: ")
        p2 = input("Vuelve a introducir la contraseña: ")
        if p1 == p2:
            print(f"Contraseñas coinciden. Intentos inválidos previos: {intentos_invalidos}")
            return
        intentos_invalidos += 1
        print("No coinciden. Inténtalo de nuevo.")

# 3. Escribir un programa que nos pida nuestro nombre y apellidos (dos peticiones
# diferentes hechas en ese orden) y nos lo escriba formateado de la siguiente forma:
# Morales Vázquez, José María
def ejercicio_3():
    nombre = input("Introduce tu nombre: ")
    apellidos = input("Introduce tus apellidos: ")
    # Suponemos que los apellidos están separados por espacios y el nombre puede tener varios
    apellidos_form = apellidos.strip()
    nombre_form = nombre.strip()
    print(f"{apellidos_form}, {nombre_form}")

# 4. Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
# espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
# que ha encontrado y suprimido.
def ejercicio_4():
    s = input("Introduce una cadena: ")
    espacios = s.count(' ')
    sin_espacios = s.replace(' ', '')
    print(f"Cadena sin espacios: {sin_espacios}")
    print(f"Espacios eliminados: {espacios}")

# 5. Escribir un programa que pida por teclado una cadena de texto y la imprima escrita al
# reves
def ejercicio_5():
    s = input("Introduce una cadena: ")
    print(s[::-1])

# 6. Escribir un programa que pida por teclado una cadena de texto y la separe en dos
# distintas. En la primera de ellas estarían las letras que ocupan una posición par y en la
# segunda las que ocupan una posición impar. (Posiciones contadas desde 0)
def ejercicio_6():
    s = input("Introduce una cadena: ")
    pares = ''.join(ch for i, ch in enumerate(s) if i % 2 == 0)
    impares = ''.join(ch for i, ch in enumerate(s) if i % 2 == 1)
    print(f"Posiciones pares: {pares}")
    print(f"Posiciones impares: {impares}")

# 7. Escribir un programa que pida por teclado una cadena de texto y la escriba con el
# alfabeto típico de los hackers sustituyendo a->4, e->3, i->1, o->0 (mayúsculas y minúsculas)
def ejercicio_7():
    s = input("Introduce una cadena: ")
    trans = str.maketrans('aeioAEIO', '43104310')
    print(s.translate(trans))

# 8. Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
# vocales.
def ejercicio_8():
    s = input("Introduce una cadena: ")
    resultado = re.sub('[AEIOUaeiou]', '', s)
    print(resultado)

# 9. Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
# Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital
# (París, Roma, Santiago de Chile o Tokio)
def ejercicio_9():
    destinos = {
        'FRANCIA': 'París',
        'ITALIA': 'Roma',
        'CHILE': 'Santiago de Chile',
        'JAPÓN': 'Tokio',
        'JAPON': 'Tokio'
    }
    elec = input("Elige destino (Francia, Italia, Chile, Japón): ")
    clave = elec.strip().upper()
    capital = destinos.get(clave)
    if capital:
        print(f"La capital de {elec.strip()} es {capital}.")
    else:
        print("Destino no reconocido.")

# 10. Valida si un NIF español introducido por teclado es correcto.
# Longitud 9: 8 dígitos + 1 letra (mayúscula o minúscula)
def validar_nif(nif: str) -> bool:
    nif = nif.strip()
    if not re.fullmatch(r"\d{8}[A-Za-z]", nif):
        return False
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(nif[:8])
    letra = nif[8].upper()
    return tabla[numero % 23] == letra

def ejercicio_10():
    s = input("Introduce un NIF (8 dígitos y una letra): ")
    if validar_nif(s):
        print("NIF válido.")
    else:
        print("NIF inválido.")

# 11. Mejorar para detectar NIF o NIE y comunicarnos el tipo y validez.
# NIE: empieza por X, Y o Z seguido de 7 cifras y una letra final
def validar_nie(nie: str) -> bool:
    nie = nie.strip().upper()
    if not re.fullmatch(r"[XYZ]\d{7}[A-Z]", nie):
        return False
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    inicial = nie[0]
    remap = {'X': '0', 'Y': '1', 'Z': '2'}
    numero = int(remap[inicial] + nie[1:8])
    letra = nie[8]
    return tabla[numero % 23] == letra

def ejercicio_11():
    s = input("Introduce NIF o NIE: ")
    ss = s.strip().upper()
    if re.fullmatch(r"\d{8}[A-Z]", ss):
        valido = validar_nif(ss)
        tipo = 'NIF'
    elif re.fullmatch(r"[XYZ]\d{7}[A-Z]", ss):
        valido = validar_nie(ss)
        tipo = 'NIE'
    else:
        print("Formato no reconocido como NIF/NIE.")
        return
    print(f"Tipo: {tipo}. Válido: {'Sí' if valido else 'No'}")

# 12. Matrículas españolas: 4 dígitos + 3 letras (mayúsculas) excluyendo vocales, Ñ y Q
def es_matricula_valida(placa: str) -> bool:
    placa = placa.strip().upper()
    # formato estricto: 4 dígitos seguidos de 3 letras
    if not re.fullmatch(r"\d{4}[A-Z]{3}", placa):
        return False
    letras = placa[-3:]
    # letras permitidas: todas las letras A-Z excepto AEIOUÑQ
    prohibidas = set(list('AEIOUÑQ'))
    for ch in letras:
        if ch in prohibidas:
            return False
    return True

def ejercicio_12():
    s = input("Introduce una matrícula (formato 1234ABC): ")
    if es_matricula_valida(s):
        print("Matrícula válida.")
    else:
        print("Matrícula inválida.")

# 13. Admitir espacio o guión entre números y letras
def es_matricula_valida_flexible(placa: str) -> bool:
    placa = placa.strip().upper()
    # permitir 1234ABC o 1234 ABC o 1234-ABC
    m = re.fullmatch(r"(\d{4})([ -]?)([A-Z]{3})", placa)
    if not m:
        return False
    numeros, sep, letras = m.group(1), m.group(2), m.group(3)
    prohibidas = set(list('AEIOUÑQ'))
    for ch in letras:
        if ch in prohibidas:
            return False
    return True

def ejercicio_13():
    s = input("Introduce una matrícula (ej. 1234ABC, 1234 ABC o 1234-ABC): ")
    if es_matricula_valida_flexible(s):
        print("Matrícula válida.")
    else:
        print("Matrícula inválida.")

# 14. Modifica el programa que validaba si un NIF era correcto comprobando si la letra
# que incorpora lo es. (Se usa la tabla de control:  "TRWAGMYFPDXBNJZSQVHLCKE")
# La comprobación ya está implementada en validar_nif y validar_nie; aquí mostramos
# un programa específico que explica la letra esperada.
def ejercicio_14():
    s = input("Introduce un NIF (8 dígitos + letra): ")
    nif = s.strip()
    if not re.fullmatch(r"\d{8}[A-Za-z]", nif):
        print("Formato inválido.")
        return
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(nif[:8])
    letra_esperada = tabla[numero % 23]
    letra_real = nif[8].upper()
    print(f"Letra esperada: {letra_esperada}. Letra proporcionada: {letra_real}.")
    if letra_esperada == letra_real:
        print("La letra es correcta. NIF válido.")
    else:
        print("La letra NO es correcta. NIF inválido.")

# 15. Valida una fecha en formato DD/MM/YYYY. Comprobamos formato, rangos y años bisiestos.
def es_bisiesto(anyo: int) -> bool:
    # Regla completa: divisible por 4, no por 100 salvo que también sea divisible por 400
    return (anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0))

def validar_fecha(fecha: str) -> bool:
    m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{4})", fecha)
    if not m:
        return False
    dia, mes, anyo = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if not (1 <= mes <= 12):
        return False
    dias_mes = [31, 29 if es_bisiesto(anyo) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not (1 <= dia <= dias_mes[mes-1]):
        return False
    return True

def ejercicio_15():
    s = input("Introduce una fecha en formato DD/MM/YYYY: ")
    if validar_fecha(s):
        print("Fecha válida.")
    else:
        print("Fecha inválida.")


# Menú

ejercicios = {i: globals()[f"ejercicio_{i}"] for i in range(1, 16)}

def menu():
    print("Ejercicios genéricos de programación 3 - menú")
    print("Introduce el número del ejercicio que quieras ejecutar (1-15) o 0 para salir.")
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
            print("Opción no válida. Elige un número entre 1 y 15 o 0 para salir.")


if __name__ == '__main__':
    menu()
