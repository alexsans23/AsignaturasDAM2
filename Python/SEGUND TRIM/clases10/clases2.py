from tokenize import String


class Perro:
    nombre = "Bobby"
    numPerros = 0
    #constructor
    def __init__(self, nombre= "Bobby"):
        self.nombre= nombre
        Perro.numPerros +=1

    #funcion de la clase
    def llamar(self):
        return("Ey " + self.nombre + " Ven aqui!")

    @classmethod
    def cuantosPerros(cls):
        return cls.numPerros

    @staticmethod
    def ladrar():
        return "Guau"

    def sobrecarga(self, atributo):
        if isinstance(atributo,int):
            print("estoy trabajabdo con un entero")
        elif isinstance(atributo,float):
            print("estoy trabajabdo con un float")
        elif isinstance(atributo,String):
            print("estoy trabajabdo con un String")
        elif isinstance(atributo,list):
            print("estoy trabajabdo con una lista")
        else:
            print("otra cosa")

    def sobrecargada2(selfself, *atributos):
        if(len())





mascota1 = Perro("Sultan")
mascota2 = Perro()
mascota3 = Perro("Toby")

print(mascota2.cuantosPerros())
print(mascota1.cuantosPerros())
print(mascota3.cuantosPerros())

print(Perro.cuantosPerros())   #despues de hacer lo de @ para depsues de lo de cls

#Perro.numPerros = 10
#print(mascota3.cuantosPerros())

print(Perro.ladrar())
print(mascota2.ladrar())

mascota3.sobrecarga(3)
mascota3.sobrecarga(3.5)
mascota3.sobrecarga("hola")
mascota3.sobrecarga(3)





