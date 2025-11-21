#diccionarios
#los diccionarios son como los map en java (clave, valor)

diccionario = {"nombre" : "Sara", "edad" : 33, "soltera" : True}


print(diccionario)

for elemento in diccionario:
    print(diccionario[elemento])

for elemento in diccionario:
    print(elemento , ":" , diccionario[elemento])

for clave, valor in diccionario.items():
    print(clave , ":", valor)

#print(diccionario.get("edad"))
#print(diccionario["edad"])   la diferencia entre estos 2 es qie cuando no existe la clave el get no da excepcion solo return 0
diccionario["asignatura"]= "Bases de Datos"
print (diccionario)

#diccionario.clear() borra el diccionario completo
#print(diccionario)

