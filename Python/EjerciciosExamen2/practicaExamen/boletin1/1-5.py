# ==========================================
print("Ejercicio1:")


# Opción 1: Usando while
num = 0
while num <= 10:
    print(num)
    num += 1


# Opción 2: Usando for
for i in range(1, 11):
    print(i)


# ==========================================
print("Ejercicio2:")

num = 0
while num <= 50:
    if num % 2 == 0:
        print(num)
    num += 1


# ==========================================
print("Ejercicio3:")

num = int(input("Introduce un número: "))  # input() devuelve str, se convierte a int manualmente
i = num
cont = 0

while cont < 5:
    if i % num == 0:
        print(i)
        cont += 1
    i += 1

print("Estos son los 5 primeros múltiplos de tu número.")


# ==========================================
print("Ejercicio4:")

for i in range(1, 100000):
    if i % 7 == 0:
        print(i)


# ==========================================
print("Ejercicio5:")

num = int(input("introduce un numero:"))

if num % 2 == 0:
    print("es par")
else:
    print("es impar")
