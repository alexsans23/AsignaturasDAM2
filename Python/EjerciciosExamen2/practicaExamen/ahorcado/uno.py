# uno_replace.py
frase = input("Introduce una frase: ")
letra = input("Letra a mantener: ")[0]

for c in frase:
    if c == letra or c == " ":
        continue
    frase = frase.replace(c, "*")

print("Resultado:", frase)


# uno_list.py
frase = input("Introduce una frase: ")
letra = input("Letra a mantener: ")[0]

res = ""
for c in frase:
    if c == letra or c == " ":
        res += c
    else:
        res += "*"

print("Resultado:", res)
