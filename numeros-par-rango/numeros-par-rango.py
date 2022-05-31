# input


X = int(input("Inserte el primer digito del rango: "))
Y = int(input("Inserte el ultimo digito del rango: "))

# processing 
par = 0
while X < Y:
    if X % 2 == 0:
        print(X)
        par = par + 1
    X = X + 1
print("\n Los numeros pares del rango son:" + str(par))

