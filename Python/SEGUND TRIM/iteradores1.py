profesores = ["Agustin", "natalia", "javier"]

iterador = iter(profesores)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador, "no hay mas profes")) # se puede en el segundo parametro poner un mensaje de expecion si no quedan cosas que iterar
