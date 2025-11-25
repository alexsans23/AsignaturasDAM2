class ClaseA:
    def __init__(self):
        self.nombre = "Clase A"

    def getNombre(self):
        return (self.nombre)


class ClaseB(ClaseA):
    #pass , antes lo pusaimos al no definir nigun metodo ya que los hereda pero a continacion los podemos sobreescribir tambien
    def __init__(self, subclase):
        super()
        self.subclase = subclase       #no he entendidid porque pero no  va bien si tenenos el __ , asi que hay que quitarlo

    def getNombre(self):

        return (self.nombre)

objetoa = ClaseA()
objetob= ClaseB()

print(objetoa.getNombre())
print(objetob.getNombre())

#esta clase rarete, no consigio nada , pasamos a herencia2