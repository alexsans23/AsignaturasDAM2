"""
Hoja de ejercicios - Ejercicios genéricos de programación 7
Incluye soluciones y comentarios detallados para cada ejercicio.
Requisitos: Python 3.10+ (para usar match/case). Si tu versión es anterior,
usa la alternativa con if/elif (comentada al final de cada caso).
"""

import random
import math
import statistics

# ---------------------------
# EJERCICIO 1 y 2: Calculadora con match/case (switch)
# ---------------------------

def calculadora_operacion(a: float, b: float, op: str):
    """
    Calculadora que acepta:
      - op puede ser 'S'/'SUM'/'+' -> suma
                   'R'/'SUB'/'-' -> resta
                   'M'/'MULT'/'*' -> multiplicar
                   'D'/'DIV'/'/' -> dividir
                   'SQ'/'SQR' -> cuadrado (solo usa 'a', ignora b)
                   'CU'/'CUBE' -> cubo (solo usa 'a')
                   'RA'/'SQRT' -> raíz cuadrada (solo usa 'a')
    Devuelve un tuple (resultado, mensaje_error_or_None).
    Comentario importante: usamos .upper() y .strip() para aceptar entradas en minúsculas
    o con espacios, lo que es más tolerante para el usuario.
    """
    # normalizamos la operación: quitamos espacios y pasamos a mayúsculas
    op_norm = op.strip().upper()

    # match/case: es el equivalente a switch. Requiere Python 3.10+
    match op_norm:
        case "S" | "SUM" | "+":
            # suma: usamos ambos operandos
            return a + b, None
        case "R" | "SUB" | "-":
            # resta
            return a - b, None
        case "M" | "MULT" | "*":
            # multiplicación
            return a * b, None
        case "D" | "DIV" | "/":
            # división: ojo con división por cero
            if b == 0:
                return None, "Error: división por cero"
            return a / b, None
        case "SQ" | "SQR" | "C" | "CUAD":  # varios alias para cuadrado
            # cuadrado: solo usamos a (b ignorado)
            return a * a, None
        case "CU" | "CUBE" | "T":  # alias para cubo
            return a * a * a, None
        case "RA" | "SQRT" | "RZ":  # alias para raíz cuadrada
            # raíz cuadrada: si a negativo en números reales da error
            if a < 0:
                return None, "Error: raíz de número negativo (no permitida en reales)"
            return math.sqrt(a), None
        case _:
            return None, f"Operación desconocida: {op}"

# Alternativa con if/elif (para Python <3.10):
# def calculadora_operacion_if(a,b,op):
#     op_norm = op.strip().upper()
#     if op_norm in ("S","SUM","+"): return a+b, None
#     elif op_norm in ("R","SUB","-"): return a-b, None
#     ...

# ---------------------------
# EJERCICIO 3: Mes por número 1-12
# ---------------------------

def nombre_mes(n: int) -> str:
    """
    Devuelve el nombre del mes para n en 1..12. Si n está fuera, devuelve mensaje de error.
    Usamos match/case para practicar el switch.
    """
    match n:
        case 1: return "Enero"
        case 2: return "Febrero"
        case 3: return "Marzo"
        case 4: return "Abril"
        case 5: return "Mayo"
        case 6: return "Junio"
        case 7: return "Julio"
        case 8: return "Agosto"
        case 9: return "Septiembre"
        case 10: return "Octubre"
        case 11: return "Noviembre"
        case 12: return "Diciembre"
        case _: return f"Error: {n} no corresponde a ningún mes (debe ser 1-12)"

# ---------------------------
# EJERCICIO 4: Nota a calificación
# ---------------------------

def calificacion_por_nota(n: int) -> str:
    """
    Recibe una nota entera entre 1 y 10 (sin decimales) y devuelve la calificación textual.
    Escala:
      1-2 -> Muy deficiente
      3-4 -> Insuficiente
      5   -> Suficiente
      6   -> Bien
      7-8 -> Notable
      9-10-> Sobresaliente
    Validamos que n sea entero y esté en 1..10.
    """
    if not isinstance(n, int):
        return "Error: la nota debe ser un entero sin decimales"
    if n < 1 or n > 10:
        return "Error: la nota debe estar entre 1 y 10"
    match n:
        case 1 | 2:
            return "Muy deficiente"
        case 3 | 4:
            return "Insuficiente"
        case 5:
            return "Suficiente"
        case 6:
            return "Bien"
        case 7 | 8:
            return "Notable"
        case 9 | 10:
            return "Sobresaliente"

# ---------------------------
# EJERCICIO 5 COMPLETO (con round)
# ---------------------------

# Pedimos al usuario el número de elementos del array
try:
    n = int(input("Introduce el número de elementos del array: "))
    if n <= 0:
        raise ValueError("El número debe ser mayor que 0")
except ValueError as e:
    print("Error de entrada:", e)
    exit()  # Salimos si el usuario no introduce un número válido

# Creamos la lista dinámica de n enteros aleatorios entre 10 y 1000
arr = [random.randint(10, 1000) for _ in range(n)]
# Comentario: list comprehension + random.randint genera n números aleatorios

# Mostramos el array generado
print("Array generado:", arr)

# Calculamos el máximo, mínimo y media
maximo = max(arr)  # máximo valor en la lista
minimo = min(arr)  # mínimo valor en la lista
media = statistics.mean(arr)  # media aritmética (float)

# Redondeamos la media a dos decimales con round()
media_redondeada = round(media, 2)

# ---------------------------
# EJERCICIO 6: Posiciones de máximo y mínimo (todas las apariciones)
# ---------------------------

def posiciones_valor(arr: list, valor: int):
    """
    Devuelve una lista con **todas** las posiciones (índices 0-based) donde aparece 'valor' en 'arr'.
    Si no aparece, devuelve lista vacía.
    """
    # Iteramos con enumerate para obtener (indice, valor_elemento)
    pos = [i for i, v in enumerate(arr) if v == valor]
    return pos

def resumen_con_posiciones(arr: list):
    """
    Calcula máximo y mínimo y devuelve:
      (maximo, posiciones_maximo, minimo, posiciones_minimo, media_str)
    donde posiciones_* son listas con todos los índices donde aparece cada uno.
    """
    if len(arr) == 0:
        raise ValueError("La lista no puede estar vacía")
    maximo = max(arr)
    minimo = min(arr)
    pos_max = posiciones_valor(arr, maximo)
    pos_min = posiciones_valor(arr, minimo)
    media_str = f"{statistics.mean(arr):.2f}"
    return maximo, pos_max, minimo, pos_min, media_str

    # Recorremos el array para calcular máximo, mínimo y suma
    for i in range(n):
        valor = arr[i]
        suma += valor
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor

    # Buscamos todas las posiciones del máximo y mínimo
    posiciones_max = []
    posiciones_min = []
    for i in range(n):
        if arr[i] == maximo:
            posiciones_max.append(i)
        if arr[i] == minimo:
            posiciones_min.append(i)

#ESTA FORMA ES MEJOR::::::::::::::::::::::
# Esto reemplaza la función "posiciones_valor" que antes no estaba definida
posiciones_max = []
posiciones_min = []

for i in range(n):
    if arr[i] == maximo:
        posiciones_max.append(i)  # guardamos el índice donde aparece el máximo
    if arr[i] == minimo:
        posiciones_min.append(i)  # guardamos el índice donde aparece el mínimo




# ---------------------------
# EJERCICIO 7: Recuperar por posición con chequeo de límites
# ---------------------------

def recuperar_posicion(arr: list, pos: int):
    """
    Recupera el elemento en la posición 'pos' (interpreto pos como índice 0-based).
    Puedes adaptar a 1-based si el examen pide posiciones humanas.
    Lanza error con mensaje si pos está fuera de rango.
    """
    # Validamos tipo
    if not isinstance(pos, int):
        raise TypeError("La posición debe ser un entero")
    if pos < 0 or pos >= len(arr):
        raise IndexError(f"Posición fuera de rango: {pos}. Valid range: 0..{len(arr)-1}")
    return arr[pos]

   #mejor forma:
# Pedimos al usuario la posición que quiere consultar
try:
    posicion = int(input(f"Introduce la posición a consultar (0 a {n - 1}): "))
except ValueError:
    print("Error: debes introducir un número entero")
    exit()

    # Comprobamos si la posición es válida
if 0 <= posicion < n:
    print(f"El valor en la posición {posicion} es:", arr[posicion])
else:
    print("Error: posición fuera de rango")


# ---------------------------
# EJERCICIO 8: Tablero buscaminas 5x5 con 5 minas aleatorias
# ---------------------------

def generar_tablero_buscaminas(filas: int = 5, columnas: int = 5, n_minas: int = 5):
    """
    Genera un tablero de 'filas' x 'columnas' con 'n_minas' minas distribuidas aleatoriamente.
    Representación:
      - 1 -> mina
      - 0 -> sin mina
    Aseguramos que no haya posición repetida para las minas.
    Retorna la matriz como una lista de listas (filas).
    """
    if n_minas > filas * columnas:
        raise ValueError("Demasiadas minas para el tamaño del tablero")

    # Inicializamos tablero con ceros
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    # Generamos n_minas posiciones únicas usando sample sobre el rango total
    # Convertimos posición indexada linealmente -> (fila, columna) con divmod
    posiciones = random.sample(range(filas * columnas), n_minas)
    for p in posiciones:
        fila, col = divmod(p, columnas)
        tablero[fila][col] = 1

    return tablero

def dibujar_tablero(tablero: list):
    """
    Imprime el tablero en formato legible, filas por línea separando con espacios.
    """
    for fila in tablero:
        print(" ".join(str(x) for x in fila))

   #MEJOR FORMA
import random


# ---------------------------
# EJERCICIO 8: Tablero de Buscaminas 5x5 con 5 minas (versión clásica)
# ---------------------------

def crear_tablero_buscaminas(filas=5, columnas=5, minas=5):
    """
    Crea un tablero de buscaminas de tamaño filas x columnas con 'minas' minas.
    Las minas se representan con 1 y las casillas vacías con 0.
    Devuelve el tablero como lista de listas.
    """

    # Creamos el tablero vacío paso a paso
    tablero = []  # lista vacía que contendrá las filas
    for i in range(filas):
        fila = []  # lista que representará cada fila
        for j in range(columnas):
            fila.append(0)  # agregamos un 0 por cada columna
        tablero.append(fila)  # agregamos la fila completa al tablero

    # Colocamos las minas de forma aleatoria
    minas_colocadas = 0
    while minas_colocadas < minas:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        if tablero[fila][columna] == 0:  # solo colocamos mina si no hay
            tablero[fila][columna] = 1
            minas_colocadas += 1

    return tablero


# Creamos el tablero
tablero = crear_tablero_buscaminas()

# Mostramos el tablero fila por fila
print("Tablero de Buscaminas:")
for fila in tablero:
    fila_str = ""
    for casilla in fila:
        fila_str += str(casilla) + " "
    print(fila_str.strip())  # .strip() elimina el último espacio extra

# ---------------------------
# EJEMPLOS DE USO / PRUEBAS SIMPLE (se pueden ejecutar)
# ---------------------------

if __name__ == "__main__":
    # Ejercicio 1 y 2 - calculadora
    print("=== Calculadora ejemplos ===")
    res, err = calculadora_operacion(10, 5, "S")   # suma
    print("10 + 5 =", res, "err:", err)
    res, err = calculadora_operacion(10, 5, "D")   # dividir
    print("10 / 5 =", res, "err:", err)
    res, err = calculadora_operacion(9, 0, "D")    # división por cero
    print("9 / 0 ->", res, "err:", err)
    res, err = calculadora_operacion(4, 0, "RA")   # raíz de 4
    print("sqrt(4) ->", res, "err:", err)
    res, err = calculadora_operacion(3, 0, "CU")   # cubo de 3
    print("3^3 ->", res, "err:", err)

    # Ejercicio 3 - meses
    print("\n=== Meses ===")
    print("3 ->", nombre_mes(3))
    print("12 ->", nombre_mes(12))
    print("-1 ->", nombre_mes(-1))

    # Ejercicio 4 - calificaciones
    print("\n=== Calificaciones ===")
    for n in [2, 4, 5, 6, 8, 10, 11]:
        print(n, "->", calificacion_por_nota(n))

    # Ejercicio 5 y 6 - array aleatorio y resumen
    print("\n=== Array aleatorio resumen ===")
    #arr = crear_array_aleatorio(10, 10, 1000)  # 10 elementos
    print("Array:", arr)
   # maximo, minimo, media = resumen_estadistico(arr)
    print("Máx:", maximo, "Mín:", minimo, "Media:", media)
    # posiciones
    maxx, posmax, minn, posmin, media2 = resumen_con_posiciones(arr)
    print("Máx:", maxx, "posiciones:", posmax, "Mín:", minn, "posiciones:", posmin, "Media:", media2)

    # Ejercicio 7 - recuperar por posición (ejemplo)
    print("\n=== Recuperar por posición ===")
    try:
        idx = 3
        val = recuperar_posicion(arr, idx)
        print(f"Valor en posición {idx} ->", val)
    except Exception as e:
        print("Error:", e)

    # Ejercicio 8 - buscaminas
    print("\n=== Buscaminas 5x5 con 5 minas ===")
    tablero = generar_tablero_buscaminas(5,5,5)
    dibujar_tablero(tablero)
