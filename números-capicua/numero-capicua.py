# input

print("------------------------------------------------")

X = int(input("Inserte un numero: "))

# processing

X1 = X
n = 0

print("------------------------------------------------")

while X1 != 0:
    n = 10 * n + X1 % 10
    X1 = X1 // 10
if n == X:
    print("Los numeros " + str(X) + " son capicúa ")
    print("------------------------------------------------")
else:
    print("Los numeros " + str(X) + " no son capicúa ")
    print("------------------------------------------------")