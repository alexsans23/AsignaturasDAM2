#Recibir por consola una fraccion, tendra que ser en este
# formato = 3/10 . Habra que devolver la solucion de la fraccion
# redondeado maximo a 3 decimales. Por ejemplo 0.333.
while True:
    fraccion = input("Escribe tu fracción: ")

    # ---------- COMPROBACIONES ----------
    if ("/" not in fraccion or             # Debe tener al menos una barra
        fraccion.count("/") > 1 or         # No puede tener más de una barra
        fraccion.startswith("/") or        # No puede empezar con "/"
        fraccion.endswith("/") or          # No puede terminar con "/"
        "." in fraccion):                   # No puede tener decimales
        print("Error: fracción no válida. Intenta de nuevo.")
        continue

    # Separar numerador y denominador
    partes = fraccion.split("/")
    numerador_str = partes[0]
    denominador_str = partes[1]

    # Comprobar que sean números
    if not numerador_str.isdigit() or not denominador_str.isdigit():
        print("Error: solo se permiten números enteros")
        continue

    numerador = int(numerador_str)
    denominador = int(denominador_str)

    # Comprobar que el denominador no sea cero
    if denominador == 0:
        print("Error: el denominador no puede ser cero")
        continue

    # ---------- TODO CORRECTO ----------
    resultado = round(numerador / denominador, 3)
    print("Solución:", resultado)
    break



###########OTRA FORMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

fraccion = input("Escribe tu fracción: ")

# ---------- COMPROBACIONES en un solo if ----------
if ("/" not in fraccion or             # Debe tener al menos una barra
    fraccion.count("/") > 1 or         # No puede tener más de una barra
    fraccion.startswith("/") or        # No puede empezar con "/"
    fraccion.endswith("/") or          # No puede terminar con "/"
    "." in fraccion or                  # No puede tener decimales
    not fraccion.split("/")[0].isdigit() or  # Numerador debe ser número
    not fraccion.split("/")[1].isdigit() or  # Denominador debe ser número
    int(fraccion.split("/")[1]) == 0        # Denominador distinto de cero
   ):
    print("Error: fracción no válida")
else:
    # Separar numerador y denominador
    numerador = int(fraccion.split("/")[0])
    denominador = int(fraccion.split("/")[1])

    # Calcular y redondear a 3 decimales
    resultado = round(numerador / denominador, 3)
    print("Solución:", resultado)
