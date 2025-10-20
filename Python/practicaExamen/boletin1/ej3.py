num = int(input("introduce un numero:"))
# input solo recibe str asi que hay que hacer un cast manual a int
i = num
cont = 0
while cont < 5:
    if i % num == 0:
        print(i)
        cont += 1
    i += 1


print("estos son los 5 primeros multiplos de tu numero ")