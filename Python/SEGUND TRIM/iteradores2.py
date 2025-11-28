
class DiasDeLaSemana:
    def __init__(self, dia):
        self.dia = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
        self.indice = dia

    def mostrar(self):
        print(self.dia[self.indice])

    def __iter__(self):
        return self

    def __next__(self):
        dia_actual = self.dia[self.indice]
        if self.indice >= len(self.dia)-1:
            self.indice= 0
        else:
            self.indice +=1
        return dia_actual


dia = DiasDeLaSemana(2)
dia.mostrar()

iterador = iter(dia)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
