numero = int(input("Ingrese un número entero: "))

for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)