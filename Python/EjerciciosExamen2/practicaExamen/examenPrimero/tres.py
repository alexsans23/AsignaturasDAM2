#Recibir una cadena de texto por consola y mostrarlo sin espacios
# en blanco y sin vocales, decir cuantas vocales han sido suprimidas
# y cuantos espacios en blanco.

frase = input("Escribe un texto:")
frase2 = ""

contVocales = 0
contEspacios = 0

for i in range(len(frase)):
    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        contVocales += 1
        continue
    elif frase[i] == " ":
        contEspacios += 1
        continue
    else:
        frase2 += frase[i]

print("Sin vocales ni espacios: ", frase2)
print("Vocales suprimidas: ", contVocales)
print("Espacios en blanco suprimidos: ", contEspacios)

#FORMA IDEALLLLLLLLLLLLLLLLLLLLL

# Recibir una cadena de texto por consola
frase = input("Escribe un texto: ")
frase2 = ""

# Contadores de vocales y espacios
contVocales = 0
contEspacios = 0

# Conjunto de todas las vocales, minúsculas y mayúsculas
vocales = "aeiouAEIOU"

for caracter in frase:
    if caracter in vocales:  # Comprobamos si es vocal
        contVocales += 1
        continue
    elif caracter == " ":     # Comprobamos si es espacio
        contEspacios += 1
        continue
    else:
        frase2 += caracter    # Lo agregamos a la nueva cadena

# Mostrar resultados
print("Sin vocales ni espacios:", frase2)
print("Vocales suprimidas:", contVocales)
print("Espacios en blanco suprimidos:", contEspacios)
