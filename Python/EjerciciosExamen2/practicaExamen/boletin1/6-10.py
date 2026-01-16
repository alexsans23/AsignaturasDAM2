# ==========================================
print("Ejercicio6")

numero = int(input("Introduce un número: "))

if numero % 3 == 0:
    print("El número", numero, "es divisible por 3.")
else:
    print("El número", numero, "NO es divisible por 3.")

# ==========================================
print("Ejercicio7")

precio = float(input("Precio: "))   #si concatenamos el print con + habra que hacer cast (str) a los num
resultado = precio + (precio*21/100)  #pero si es con "," no hace falta
print("Resultado: ", resultado) #tambien se hace asi, las variqables entre {}, y no hace falta , ni + ni str


# ==========================================
print("Ejercicio8")

importe = float(input("Introduce el importe total a pagar (€): "))
meses = int(input("Introduce el número de meses: "))
pago_mensual = importe / meses
print("Deberás pagar", round(pago_mensual, 2), "€ cada mes.")

# ==========================================
print("Ejercicio9")

import random
numero = random.randint(0,50)
print(numero)

# ==========================================
print("Ejercicio10")
import random
dado1=0
dado2=0

