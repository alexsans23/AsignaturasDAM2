class Perro:
    nombre = "Bobby"

    #constructor
    def __init__(self, secreto, secretisimo, nombre= "Bobby"):
        self.nombre= nombre
        self.secreto = secreto
        self.secretisimo = secretisimo

    #funcion de la clase
    def llamar(self):
        return("Ey " + self.nombre + " Ven aqui!")


#mascota1 = Perro()
#print(mascota1.llamar())

#mascota2 = Perro("Sultan")
#print(mascota2.llamar())

#mascota1.nombre= "alex"
#print(mascota1.llamar())

mascota2 =  Perro("cuchi", "mi bebe", "Sultan")
print(mascota2.llamar())
mascota2._secreto = "engendro"
print(mascota2._Perro_secreto)
mascota2._Perro__secretisimo = "rata azmilclera"
print(mascota2.__secretisimo)



