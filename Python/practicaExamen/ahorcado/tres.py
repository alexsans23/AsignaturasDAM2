# 3. Versión completa del juego:
# - Pedirá letras hasta que la frase esté completa.
# - Mostrará cuántas veces aparece cada letra.
# - Cuando se complete la frase, mostrará un mensaje de victoria con los intentos usados.
# Ejemplo:
# ...
# Resultado: la lluvia en sevilla es una *ura *aravilla
# Introduce una letra: p
# La letra p aparece en 1 ocasiones
# Resultado: la lluvia en sevilla es una pura *aravilla
# Introduce una letra: m
# La letra m aparece en 1 ocasiones
# Resultado: la lluvia en sevilla es una pura maravilla
# Has ganado. Has necesitado 11 intentos para completar la frase.

frase = input("Introduce una frase: ")
letra_mantener = input("Letra a mantener: ")[0]

# Crear panel inicial
panel = ""
for c in frase:
    if c == letra_mantener or c == " ":
        panel += c
    else:
        panel += "*"

print("Resultado:", panel)

intentos = 0
while "*" in panel:
    letra = input("Introduce una letra: ")[0]
    intentos += 1
    contador = 0
    nuevo_panel = ""

    for i in range(len(frase)):
        if frase[i] == letra:
            contador += 1
            nuevo_panel += letra
        else:
            nuevo_panel += panel[i]

    panel = nuevo_panel
    print(f"La letra {letra} aparece en {contador} ocasiones")
    print("Resultado:", panel)

print(f"Has ganado. Has necesitado {intentos} intentos para completar la frase.")
