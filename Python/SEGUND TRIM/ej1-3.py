"""
1. Crear un programa o una función que reciba un diccionario con los datos de los clientes de una tienda
y su edad y los muestre por consola ordenados por nombre de pila. El diccionario, ya creado en el
código de tu programa, tendrá esta forma
clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto,
Francisco": 44, "Cotón, Carmelo": 56 }
Y la salida por consola así:
Carmelo Cotón (56)
Francisco Rupto (44)
José Chuletón (35)
Rubén Tosidad (27)
"""
clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto, Francisco": 44, "Cotón, Carmelo": 56 }

def mostrarClientes(clientes):
    for clave, valor in clientes.items():
        clave2 = clave.replace(",", "")
        print(clave2 , " (", valor , ")")

"""
2. Añade una función que sirva para añadir nombres al diccionario. La llamada a la función sería así:
nuevoCliente(clientes, “Felipe”, “Lotas”, 76)
Tu función debería de añadir el nuevo cliente al diccionario con el formato correcto. Si este cliente ya
existe debería de mostrar en consola un mensaje advirtiéndolo y preguntando si se quiere
sobreescribir la edad o no. 
"""
def nuevoCliente(clientes, nombre, apellido, edad):

    nombreCompleto = nombre + ", " + apellido

    for clave, valor in clientes.items():
        if nombreCompleto == clave:
            opcion = input("el cliente ya existe en el diccionario, quieres sobreescribir la edad? S/N")
            while opcion 




nuevoCliente(clientes, "Felipe", "Lotas", 76)