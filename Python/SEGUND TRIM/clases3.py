class Empleado:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__edad = edad #para que sea lo mas protegido posible

    @property          # estas cosas hay que ponerlas delante de cada metodo (los deocradores?)
    def edad(self):
        return (self.__edad)  #los guines son completamente visuales


    @edad.setter
    def edad(self, NuevaEdad):
        self.__edad = NuevaEdad

    def __str__(self):  #cuando uso un metodo magico asi lo estoy sobreescribiendo
        return (self.apellidos + ", "+ self.nombre)

# aqui no es como en java escribiendo get y set , usamos los metodos esos @ para definirlos, realmente es un apaño
emp1 = Empleado("Jose Maria", "Morales" , 57)
print(emp1.edad)

emp1.edad = 58   #daria error sin la funcion sobrecaargada

print(str(emp1))




x = 5
print(x)
del x
#print(x)  del , es un destructor, elimina variables y objetos
#del emp1

