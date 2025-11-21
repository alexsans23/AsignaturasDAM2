import random

d1 = dict(Sara = 33, Pepe =55, Luid = 55, Manolo = 33, Eva = 66, Ines = 55)

def eliminarAlAzar(d1):

    claves = list()

    for elemento in d1:
        claves.append(elemento)
    borrar = random.choice(claves)

    print(borrar)
    d1.pop(borrar)
    print(d1)


#LAS LSITAS SE PASAN SIMEPRE POR REFERENCIA NO POR VALOR , Y LOS DICCIONARIOS TAMBIEN


eliminarAlAzar(d1)


#dato = en python no hay contastes, te lo pones en mayuscula yte lo imaginas

#otra forma
mi_diccionario = {"nombre": "Ana", "edad": 22, "pais": "España"}

lista_claves = list(mi_diccionario.keys())

print(lista_claves)



texto = str(d1)
print("en texto:", texto)
