# Este arhivo .py se podria haber hecho en Jupyter Notebook pero no me da tanto tiempo para pasarlo como sera
# un poco caotico los input pero por lo demas esta la estructura basada a cada ejercicio para mas info lo pasare con
# el PDF que estara para el final de la semana

# 1. Escribir un programa que pida una contraseña por teclado (dos veces) y si no
# coinciden nos lo vuelva a pedir hasta que lo hagan

while True:
    contraseña = str(input("Ejercicio 1: Añade la contraseña: "))
    contraseñaRepetida = str(input("Ejercicio 1: Añada la contraseña correcta: "))
    if contraseña in contraseñaRepetida:  # En vez del in tambien se puede con contraseña == contraseñaRepetida
        print("Contraseña Correcta")
        break  # Lanzamos un break para acabar el bucle while
    else:
        print("Contraseña Incorrecta")

# 2. Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
# informe del número de intentos inválidos

count = 0
while True:  # Definimos una while True para que se ejecute
    contraseña = str(input("Ejercicio 2: Añade la contraseña: "))
    contraseñaRepetida = str(input("Ejercicio 2: Añada la contraseña correcta: "))
    if contraseña in contraseñaRepetida and len(contraseña) == len(contraseñaRepetida):
        print(f"Contraseña correcta numero de intentos {count}")
        break
    else:
        print("Contraseña Incorrecta")
        count += 1

# 3. Escribir un programa que nos pida nuestro nombre y apellidos (dos peticiones
# diferentes hechas en ese orden) y nos lo escriba formateado de la siguiente forma:
# Morales Vázquez, José María

nombre = str(input(
    "Ejercicio: 3 Añada su nombre: "))  # Definimos una variable input en la cual guardaremos lo que se nos pase por teclado y usamos str
apellido = str(input("Ejercicio: 3 Añada su apellido: "))  # Lo mismo que el anterior solo que con apellido

print(apellido + ", " + nombre)  # Imprimimos primero el apellido y despues el nombre
print(apellido, nombre,
      sep=", ")  # Usamos sep para definir el separador, en este caso seria = ", " entre los valores al imprimir

# Otras formas de hacerlo, NO DADAS EN CLASE

print(", ".join(["Con join: " + input("Apellidos: "), input("Nombre: ")]))
print("Con format: {}, {}".format(apellido,
                                  nombre))  # Con el metodo format con los {} se le pasa los argumentos que en nuestro
# caso serian las variables {apellido}, {nombre}
print(f"Con printf: {apellido}, {nombre}")

# 4. Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
# espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
# que ha encontrado y suprimido.

# Manera Normal

count = 0  # Definimos una variable con valor 0 que sera la que cuente los espacios
entrada = str(input("Ejercicio: 4 Escriba una cadena de texto: "))  # Pedimos entrada al usuario con valor de salida str
for i in range(0, len(entrada)):  # Usamos un for de 0, a la longitud la cadena que pasa el usuario
    if entrada[i] == " ":  # Validamos que haya espacios iterando sobre nuestra cadena
        # igual que con js se puede recorrer los caracteres de una cadena mediante su indice e 1 a 2, etc
        count += 1  # Sumamos uno al contador

print(f"La cadena es: {entrada.replace(" ", "")} el numero de espacios omitidos es de: {count} espacios")

# Otra forma

entrada = str(input("Ejercicio: 4 Extra, Escriba una cadena de texto: "))
numEspacios = entrada.count(" ")  # con el metodo count lo usamos para contar que nuestra
# variable contenga espacios y se guarda el numero en ella si hay dos espacios la variable contendra 2
print(f"La cadena es: {entrada.replace(" ", "")} el numero de espacios omitidos es de: {count} espacios")

# 5. Escribir un programa que pida por teclado una cadena de texto y la imprima escrita al
# reves (es decir, si el usuario escribe Hola Mundo el programa debería de escribir
# odnuM aloH)

# Manera normal
cadena = str(input("Ejercicio 5: Añada una cadena de texto: "))
print(cadena[::-1])  # Con una substring [INICIO:FIN:PASOS] ponemos -1 en pasos para que recorra la cadena a la inversa

# Manera sin Substring
cadena = str(input("Ejercicio 5 Extra: Añada una cadena de texto: "))
cadenaInvertida = ""
for i in range(len(cadena) - 1, -1,
               -1):  # el range de los for tiene diferentes parametros que son simililares a un substring
    # [START,STOP,PASOS] nuestro inicio es len(cadena) - 1 esto coge el ultimo valor de la cadena como iniciador
    # el STOP que es el fin lo ponemos a -1 lo podriamos poner que acabe en 0 ya que vamos en inversa pero no cogeria el ultimo caracter
    # y los PASOS en -1 para que recorra a la inversa
    cadenaInvertida += cadena[i]  # Añadimos en una variable el resultado

print(cadenaInvertida)

# 6. Escribir un programa que pida por teclado una cadena de texto y la separe en dos
# distintas. En la primera de ellas estarían las letras que ocupan una posición par y en la
# segunda las que ocupan una posición impar. Por ejemplo, si el usuario escribe Hola
# Mundo la primera cadena sería Hl ud y la segunda oaMno

entrada = str(input("Ejercicio 6: Introduce una cadena de texto: "))
pares = entrada[1::2]  # Cogemos los impares
impares = entrada[::2]  # Cogemos los pares

print(f"Los impares son {impares} y los pares son {pares}")

# 7. Escribir un programa que pida por teclado una cadena de texto y la escriba con el
# alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
# el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
# las vocales pueden estar escritas en mayúsculas o minúsculas, pero no hace falta que
# tengas en cuenta que además podrían ir acentuadas

cadena = str(input("Ejercicio 7: Añada una cadena: "))
cadena1 = ""

# Con un condicional que compare las letras y a cadena1 se le implementen los numeros
for _ in cadena:
    if _ == 'a' or _ == 'A':
        cadena1 += '4'
    elif _ == 'e' or _ == 'E':
        cadena1 += '3'
    elif _ == 'i' or _ == 'I':
        cadena1 += '1'
    elif _ == 'o' or _ == 'O':
        cadena1 += '0'
    else:
        cadena1 += _

print("Texto hackerizado:", cadena1)

cadena = str(
    input("Ejercicio 7 Extra: Añada una cadena: "))  # En la parte de abajo cuando se define la variable cadenaHackeada
# se usa el \ para dar un salto de linea y que permita poner abajo los metodos anidados porque sino seria muy poco legibre
# cadena.replace("a", "4").replace("A", "4").replace("e", "3") etc
cadenaHackeada = cadena.replace("a", "4").replace("A", "4") \
    .replace("e", "3").replace("E", "3") \
    .replace("i", "1").replace("I", "1") \
    .replace("o", "0").replace("O", "0")

print(cadenaHackeada)

# 8. Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
# vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”.

cadena = str(input("Ejercicio 8: Añada una cadena: "))

cadenaSinVocales = cadena.replace("a", "").replace("A", "") \
    .replace("e", "").replace("E", "") \
    .replace("i", "").replace("I", "") \
    .replace("o", "").replace("O", "") \
    .replace("u", "").replace("U", "")

print(f"Ejercicio 8 resultado: {cadenaSinVocales}")

# 9. Escribir un programa que nos pida elegir entre cuatro destinos turísticos (Francia,
# Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la capital de
# nuestro destino (París, Roma, Santiago de Chile o Tokio)

entrada = str("Ejercicio 9: Introduzca un pais, Francia, Italia, Chile, Japon: ")

match entrada:
    case "Francia":
        print("La capital es París")
    case "Italia":
        print("La capital es Roma")
    case "Chile":
        print("La capital es Santiago de Chile")
    case "Japón":
        print("La capital es Tokio")
    case _:
        print("Destino no reconocido")

# MANERA NORMAL CON LISTAS

entrada = str(input("Ejercicio 9 Extra: Introduzca un pais, Francia, Italia, Chile, Japon: "))

paises = ["Francia", "Italia", "Chile", "Japon"]  # Creamos una lista con los paises
capitales = ["Paris", "Roma", "Chile", "Tokio"]  # Creamos una lista con las capitales

if entrada in paises:  # Verificamos que se le pase Pais == Pais
    index = paises.index(
        entrada)  # Creamos una variable index y le pasamos la variable al indice para encontrar el valor
    print("La capital es",
          capitales[index])  # Y despues se lo pasamos a capitales[index] que es la variable que hemos guardado
    # el indice
else:
    print(f"Destino no encontrado {entrada}")

# MANERA NO DADA EN CLASE hay muchas formas para plantearnos hacer esto con diccionarios estructura de datos
# que son clave:valor, pero esto no lo enseñare xq es mas avanzado pasare una lista de todo el contenido de listas.

entrada = str(input("Ejercicio 9 Extra: Introduzca un pais, Francia, Italia, Chile, Japon: "))

paises = ["Francia", "Italia", "Chile", "Japon"]  # Creamos una lista con los paises
capitales = ["Paris", "Roma", "Chile", "Tokio"]  # Creamos una lista con las capitales

for paises, capitales in zip(paises,
                             capitales):  # Con la funcion integrada zip nos permite pasarle un conjunto de listas
    # y poder con ella iterar multiples en un for
    if entrada == paises:
        print(f"Capital encontrada {capitales}")
        break
    else:
        print(f"Pais no encontrado {paises}")

# 10. Escribe un programa que valide si un NIF español introducido por teclado es correcto.
# La longitud exacta de la cadena ha de ser de 9 caractéres. Los ocho primeros han de
# ser números comprendidos entre el 0 y el 9 y el último una letra que puede estar
# escrita en mayúsculas o minúsculas.

dni = str(input("Ejercicio 10: Introduzca un NIF español: "))

numeros = dni[:8]  # Cogemos desde 0 a 8 los numeros 23232323
letra = dni[-1]  # Cogemos el ultimo valor de dni que seria la letra A

if len(dni) == 9:
    if numeros.isdigit() and letra.isalpha():  # Verificamos que sea que contenga valores numericos y que letra sea letras
        print(f"El DNI es valido: {dni}")
    else:
        print(f"El DNI no es valido: {dni}")
else:
    print("No tiene 9 caracteres")

# 11. Mejorar el programa anterior para que detecte si se trata de un NIF o un NIE y nos
# comunique, además de si es válido de que tipo es.Un NIE es una cadena de 9 caractéres que siempre empieza por X,Y o Z y a
# continuación vienen 7 cifras y una letra final. Las letras inicial y final pueden estar
# escritas con mayúsculas o con minúsculas

dni = str(input("Ejercicio 11: Introduzca un NIF o NIE español: "))

numeros = dni[:8]
letra = dni[-1]

if len(dni) == 9:
    if numeros.isdigit() and letra.isalpha():
        print(f"El DNI es valido: {dni}")
    else:
        print(f"El DNI no es valido: {dni}")
else:
    print("No tiene 9 caracteres")

# 12. Las matrículas españolas constan de un número de cuatro dígitos y tres letras
# cual es quiera en mayúsculas a excepción de las vocales, la Ñ y la Q. Escribe un
# programa que detecte si una matrícula introducida por teclado es válida o no.

matricula = str(input("Ejercicio 12: Añada su matricula: "))
numeros = matricula[:4]  # Cogemos del inicio 0 : y el FIN 4 cogera 2343
letras = matricula[4:7].upper()  # Hacemos en mayusculas las ultimas letras de la matricula

if numeros.isdigit() and letras.isalpha() and "Ñ" not in letras and "Q" not in letras:
    print(f"Matricula valida {matricula}")
else:
    print(f"Matricula no valida {matricula}")

# 13. Modifica el programa anterior contemplando que entre los números y las letras
# podría haber un espacio en blanco (uno solo) o un guión. En ambos casos se
# considerará también que la matrícula es válida (si cumple todo lo demás, claro)

matricula = str(input("Ejercicio 13: Añada su matricula: "))
numeros = matricula[:4].upper()
letras = matricula[4:7]

if numeros.isdigit() and letras.isalpha() and "Ñ" not in letras and "Q" not in letras:
    print(f"Matricula valida {matricula}")
else:
    print(f"Matricula no valida {matricula}")

# 14. Modifica el programa que validaba si un NIF era correcto comprobando si la letra que
# incorpora lo es. La forma de hacerlo es la siguiente

nif = input("Introduce tu NIF (8 números y 1 letra): ")

if len(nif) == 9 and nif[:8].isdigit() and nif[-1].isalpha():
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numero = int(nif[:8])
    letra_correcta = letras[numero % 23]

    if nif[-1].upper() == letra_correcta:
        print("El NIF es correcto.")
    else:
        print(f"La letra es incorrecta. Debería ser: {letra_correcta}")
else:
    print("Formato inválido. Debe tener 8 números y 1 letra.")

# 15. Escribe un programa que reciba por teclado una fecha en el formato DD/MM/YYYY. El
# programa debe de comprobar si la fecha es correcta teniendo en cuenta:
# Qué el formato sea el correcto
# Que la fecha sea totalmente válida teniendo en cuenta incluso los años que son
# bisiestos (aquellos que son divisibles entre cuatro).

fecha = input("Ejercicio 15: Añada una fecha (DD/MM/YYYY): ")  # Pedimos al usuario que nos pase una fecha

if len(fecha) == 10 and fecha[2] == '/' and fecha[5] == '/':
    dia, mes, año = fecha.split('/')

    if dia.isdigit() and mes.isdigit() and año.isdigit():
        dia = int(dia)
        mes = int(mes)
        año = int(año)

        if mes == 2:  #
            dias_mes = 29 if año % 4 == 0 else 28
        elif mes in (4, 6, 9, 11):  # Validamos que los meses que tienen 30 dias
            dias_mes = 30
        else:
            dias_mes = 31  # Los dias que tengan 31 dias

        if 1 <= mes <= 12 and 1 <= dia <= dias_mes:  # Validamos la longitud de los meses y dias 1 al 12 y 1 a 31
            print(f"La fecha es correcta {fecha}")
        else:
            print(f"La fecha no es válida {fecha}")
    else:
        print("Día, mes y año deben ser números.")
else:
    print("Formato incorrecto. Usa DD/MM/YYYY.")






