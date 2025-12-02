import random

class Pokemon:
    def __init__(self, nombre):
        self._nombre = nombre
        self.__evolucion = None
        self._puntosVida = random.randint(50,100)


    def cambiarVida(self, vidaNueva):
        self._puntosVida = vidaNueva


    def setEvolucion(self, pokemon):
        self.__evolucion = pokemon

    def mostrar(self):
        print(self._nombre, "- pv: ", self._puntosVida)

    def evoluciona(self):
        if self.__evolucion == None:
            print("este pokemon n osabe evolucionar")
            evo =self
        else:
            evo = self.__evolucion
        return evo

    def combatir(self, pokemon2):

        while pokemon2._puntosVida > 0 and self._puntosVida >0:

            ataque = random.randint(25, 50)
            pokemon2.cambiarVida(pokemon2._puntosVida - ataque)
            print(self._nombre , " le ha quitado ", ataque , " puntos de vida a ", pokemon2._nombre + "!!!!")

            if (pokemon2._puntosVida <= 0):
                print("ganador : " , self._nombre)
                break

            ataque2 = random.randint(25, 50)
            self.cambiarVida(pokemon2._puntosVida - ataque2)
            print(pokemon2._nombre, " le ha quitado ", ataque2, " puntos de vida a ", self._nombre + "!!!!")

            if (self._puntosVida <= 0):
                print("ganador : " , pokemon2._nombre)
                break



#p1 = Pokemon("Bulbasaur")
#p2 = Pokemon("Venasaur")
#p1.setEvolucion(p2)

#p1.mostrar()
#p2.mostrar()

#p2 = p2.evoluciona()
#p1 = p1.evoluciona()

#p1.mostrar()
#p2.mostrar()

p3 = Pokemon("Garchomp")
p4 = Pokemon("Tyranitar")
p3.mostrar()
p4.mostrar()

p3.combatir(p4)

