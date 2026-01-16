from logging.config import dictConfigClass

d3 = dict(Primero = 'Uno')
d3["Segundo"] = "Dos"
print(d3)

dict3 = {}
d2 = dict()

print(d3)
print(d3.keys)

diccionario = {"nombre" : "Sara", "edad" : 33, "soltera" : True}

print(diccionario.get("Titulo", "No encotrado"))  # el segubndo parametro es opcional , si no lo tienen devolvera nonoe si no esta y ya

#eliminaciones

print(diccionario.pop("edad"))  #elimina un valor y ademas lo muestra
print(diccionario)


print(d3.popitem()) # elimina el ultimo insertado

#hacer una funcion para que haga lo que hacia popitem antes de la version 3.4

#no se puede añadir en el mapa valores en la posicion que tu quieres porque no va por posiciones va por claves
# duda , se puede recorer con un for in range?


diccionario.update(d3) #si metes eleemtos duplicados sutituyen al anteriior y si no lo añaden
print(diccionario)




