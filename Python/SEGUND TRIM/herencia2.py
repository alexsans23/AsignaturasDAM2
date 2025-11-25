from herencia1 import objetoa


class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"
        self.codigo = 55

    def cambiarNombre(self,nuevoNombre):
        self.nombre = nuevoNombre

    def queSoy(self):
        print("soy  clase a")

class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.subclase = "Clase B"

    def queSoy(self):
        print("soy  clase b")

    def incrementarCodigo(self):
        self.codigo += 1

class CalseC(ClaseA, ClaseB):
    pass


class CalseD(ClaseA, ClaseB):
    pass


objetoa = ClaseA()
objetob = ClaseB()

print(objetoa.nombre)
print(objetob.nombre)

print(objetob.subclase)

