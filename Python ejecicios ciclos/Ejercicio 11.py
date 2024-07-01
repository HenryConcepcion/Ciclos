numero = int(input("Ingrese un número entero de dos dígitos: "))

decenas = numero // 10
unidades = numero % 10

for i in range(decenas, unidades + 1):
    print(i)