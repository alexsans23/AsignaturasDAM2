frase = input("Introduce una frase")
letra = input("introduce la letra que si quieres mantener")

fraseArray = frase.strip()

for i in range (len(frase)):
    if fraseArray[i] is not (letra):
        fraseArray[i] == '*'


nuevaFrase= ''.join(fraseArray)
print(nuevaFrase)
