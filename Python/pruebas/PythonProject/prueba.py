opcion = input("P para jugar, C para configurar o X para salir:")
match opcion:
    case "P" | "J":  #en java se puede conctenar cas eporque hasta que no encuentre break no sale
        print("has elegido jugar")
    case "C":
        print("has elegido configurar")
    case "X":
        print("has elegido salir.Hasta la porxima")
    case _:
        print("opcion no valida")
print("fin del menu")