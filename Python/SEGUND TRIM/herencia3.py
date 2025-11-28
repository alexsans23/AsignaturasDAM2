from abc import abstractmethod, ABCMeta


class ClaseAbstracta(metaclass=ABCMeta):
    def metodoChorra(self):
        print("Hola, hola")

    @abstractmethod
    def metodoAbstracto(self):
        pass

nuevo = ClaseAbstracta()
nuevo.metodoChorra()
