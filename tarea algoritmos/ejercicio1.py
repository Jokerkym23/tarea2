#pide un nombre

nombre = input("¿Cuál es tu nombre? ")

# Pide un número entero
numVeces = int(input("escriba un numero "))

# Imprime el nombre la cantidad de veces que se pide
for i in range(numVeces):
    print(f"{numVeces}. {nombre}")
