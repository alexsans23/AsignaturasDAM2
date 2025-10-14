print("Hola mundo")
# esto es un comentario
"""
otro comentario
"""

nombre = input("dime tu nombre")
apellidos = input("dime tus apellidos")
edad = input("dime tu edad")
print( "te llamas", nombre, " tus apellidos son ", apellidos , " y tienes " , edad ," años.")

if(edad == "60"):
    print("ya deberias estar jubilado")
else:
    pass
print ("no se")
print("no se otra vez")

#de tipo int...
edad = 56
if edad>150:
    print("seguro estas vivo?")
elif edad > 68:
    print ("deberias estar jubiladoooo")
elif edad > 50 and edad < 58:
    print("Animo que queda poco")
else:
    print("no te queda na")

print("fin del programa")