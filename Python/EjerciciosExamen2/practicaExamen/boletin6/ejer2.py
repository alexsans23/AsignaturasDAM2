import re

#Validar un código postal de Madrid. Cinco números, los dos primeros siempre son el 28
#Ejemplo: 28032

entrada = str(input("Ejercicio 1: Introduce un codigo postal: "))
regex = r"^[0-9]{5}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")


#Validar un número de teléfono
#Ejemplo: 91345566

entrada = str(input("Ejercicio 2: Introduce un numero telefonico: "))
regex = r"^[1-9]{8}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")

#Validar un número de teléfono móvil (debe de empezar por 6, 7 u 8)
#Ejemplo: 655776655

entrada = str(input("Ejercicio 3: Introduce un numero telefonico: "))
regex = r"^[6-8]\\[0-9]{8}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")

#Validar un número de teléfono con prefijo internacional (empieza por el signo + seguido
#de dos dígitos, luego un espacio y a continuación un número de teléfono.
#Ejemplo +34 912233444

entrada = str(input("Ejercicio 4: Introduce un numero telefonico con prefijo: "))
regex = r"^\+\d{2}\s\d{9}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")


#Validar dos palabras de cualquier tamaño separadas por un único espacio en blanco.
#Las palabras no pueden contener números y deben de empezar ambas por una letra
#mayúscula.
#Ejemplo: Hola Mundo

entrada = str(input("Ejercicio 5: Introduce algunas palabras: "))
regex = r"^[A-Z][a-zA-Z]* [A-Z][a-zA-Z]*$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")

#Una clave con el siguiente formato XX00-xxX-00 donde las X deben de ser letras
#mayúsculas, las x letras minúsculas y los 0 d´ígitos.

entrada = str(input("Ejercicio 6: Introduce una clave: "))
regex = r"^[A-Z]{2}\d{2}-[a-z]{2}[A-Z]{1}-\d{2}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")


#Validar una tarjeta de crédito: cuatro grupos de cuatro números cada uno separados por
#un espacio. A continuación un espacio y la fecha de caducidad en formato MM/YY. El
#mes tiene que ser válido (entre 01 y 12)

# Ejemplo: 1234 5678 9012 3456 03/25

entrada = str(input("Ejercicio 7: Introduce una tarjeta de credito: "))
regex = r"^\d{4}\s\d{4}\s\d{4}\s\d{4}\s(0[1-9]|1[0-2])/\d{2}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")


#Un IBAN bancario de España. Las dos letras iniciales siempre tienen que ser ES
#Ejemplo: ES61 1234 3456 42 0456323532

entrada = str(input("Ejercicio 8: Introduce un IBAN Español: "))
regex = r"^([E][S])\d{2}\s\d{4}\s\d{4}\s\d{2}\s\d{10}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")


#Un número de 4 cifras mínimo y 8 cifras máximo
#Ejemplo: 12345

entrada = str(input("Ejercicio 9: Introduce un numero: "))
regex = r"^\d{4,8}$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")


#Una dirección IP pública de clase C. Cuatro bytes en formato decimal separados por un
#punto. Los dos primeros tienen que ser siempre 192.168.

#Ejemplo: 192.168.30.30

entrada = str(input("Ejercicio 10: Introduce la IP con el formato valido: "))
regex = r"^([1][9][2]).([1][6][8].\d{1,3}.\d{1,3})$"

if re.search(regex, entrada):
    print("valido")
else:
    print("no valido")
