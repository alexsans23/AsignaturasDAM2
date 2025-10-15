import random

#azar = random.randint(1, 6)
#print(azar)
#i = 0

#while i < 10:   #las condiciones en phyton no van entre parentesis , ejecutara aun asi
    #print(i)
    #i+=1  # en phyton no funciona el ++
cont = 0

dado1 = 1
dado2 = 0
while dado1 != dado2:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    cont+=1

print(cont)
texto = "Hola mundo"
print(len(texto))
print(texto[3:8])
print(texto[:8])
print(texto[-2])