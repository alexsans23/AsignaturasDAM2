import random

# 1 Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
# ninguno de ellos esté repetido (simulando una lotería primitiva).

# Manera facil

randomNumbers = random.sample(range(1, 49), 6)
print(f"randomNumbers Facil: {randomNumbers}")

# Manera normal

randomNumbers = []  # Declaramos una lista vacia

for _ in range(6):
    num = random.randint(1, 49)  # declaramos una variable de numeros aleatorios
    for num in randomNumbers:
        num = random.randint(1, 49)
    randomNumbers.append(num)

print(f"randomNumbers Normal: {randomNumbers}")

# 2. Hacer un programa en que nos permita calcular todos los divisores comunes a dos
# números

input1 = int(input("Ejercicio 2: Añade el primer numero para calcular su division: "))
input2 = int(input("Ejercicio 2: Añade el segundo numero para calcular su division: "))
divisores = []

for i in range(1, min(input1, input2) + 1):
    if input1 % i == 0 and input2 % i == 0:
        divisores.append(i)

print(divisores)

# 3. Escribir un programa que cuenta las palabras que tiene una frase introducida
# previamente por teclado. Las palabras pueden estar separadas por más de un espacio
# pero siempre debe de haber al menos uno. No tenemos en cuenta los signos de
# puntuación como separadores.

count = 1  # a aa a
frase = str(input("Ejercicio 3: Introduce una frase: "))
for _ in range(0, len(frase)):
    if frase[_] == " ":
        count += 1
print(f"El numero de palabras es de {count}")

# 4. Escribir un programa que nos pida una cadena por teclado y luego cuente cuantas
# palabras hay en ella con cuatro o más vocales diferentes. Por ejemplo, si introducimos
# la frase “Crisis constitucional por culpa del murcielago guineoecuatorial” Nos debería
# de decir que 3. Tendrías que tener en cuenta que las vocales pueden ir en mayúsculas
# o no y son la misma letra. Presupón que ninguna vocal va acentuada de ninguna
# forma.

frase = input("Ejercicio 4: Introduce una frase: ")
countVocales = 0

for palabra in frase.split():
    vocales_en_palabra = ""  # Guardamos las vocales diferentes encontradas
    for letra in palabra:
        if letra in "aeiouAEIOU" and letra.lower() not in vocales_en_palabra:
            vocales_en_palabra += letra.lower()  # Comprobamos las vocales que esten nuestra frase
    # Si hay 4 o más vocales diferentes, sumamos 1
    if len(vocales_en_palabra) >= 4:
        countVocales += 1

print(f"Número de palabras con 4 o más vocales diferentes: {countVocales}")

# 5. Escribe un programa que genere 100 números aleatorios comprendidos entre el 1 y
# 50 (ambos inclusive) y, posteriormente, obtenga el mayor, el menor y el que mas veces
# se repite (y nos diga cuantas veces lo hace).

randomNumbers = random.sample(range(1, 50), 30)  # Genera valores entre el 1 y 50, 100 veces variables
maximo = max(randomNumbers)  # Sacar numero maximo de la lista
minimo = min(randomNumbers)  # Sacar numero minimo de la lista
veces_repetidas = list(randomNumbers)  # Convertimos veces_repetidas a una lista
for i in range(1, 100):
    veces_repetidas.count(i)  # Sacar el numero mas repetido

print(f"""El valor maximo es: {maximo} el valor minimo es: {minimo} 
      \t el valor que se repite mas veces {veces_repetidas}""")

# 6. Escribe un programa que nos permita contar el número de veces que se repite cada
# cifra en un número. Por ejemplo, el número 885210003 tiene tres 0, un 1, un 2, un 5 y
# dos 8.

numero = input("Ejercicio 6: Inserte un número: ")
cifras = []

for i in numero:
    if i not in cifras:
        total = numero.count(i)
        print(f" El numero de veces que a salido {i} son {total}")
        cifras.append(i)
