# 2. Partiendo del ejercicio anterior:
# - Pedirá una letra por teclado.
# - Indicará cuántas veces aparece en el panel.
# - Mostrará la frase con las apariciones de esa letra sustituidas.
# - Este proceso se hace una sola vez.
# Ejemplo:
# Introduce una letra: e
# La letra e aparece en 3 ocasiones
# Resultado: l* ll**** e* *e**ll* e* *** **** ******ll*

frase = input("Introduce una frase: ")
letra_mantener = input("Letra a mantener: ")[0]

# Crear el panel inicial
panel = ""
for c in frase:
    if c == letra_mantener or c == " ":
        panel += c
    else:
        panel += "*"

print("Resultado:", panel)

# Pedir una letra y actualizar el panel
letra = input("Introduce una letra: ")[0]
contador = 0
nuevo_panel = ""

for i in range(len(frase)):
    if frase[i] == letra:
        contador += 1
        nuevo_panel += letra
    else:
        nuevo_panel += panel[i]

print(f"La letra {letra} aparece en {contador} ocasiones")
print("Resultado:", nuevo_panel)
