class Cuenta:
    def __init__(self, titular, saldo):
        self.__titular=[]
        self.__titular.append(titular)
        self.__saldo= saldo

    @property
    def titular(self):
        return(self.__titular)

    @property
    def saldo(self):
        return (self.__saldo)

    def __add__(self, cuenta):
        self.__saldo = self.__saldo + cuenta.__saldo
        self.__titular = self.__titular + cuenta.__titular
        return self


c1 = Cuenta("jose maria Morales", 1234.66)
c2 = Cuenta("maria Rodriguez", 345.78)

print(c1.titular)
c1= c1+ c2