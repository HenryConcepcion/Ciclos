numero = int(input("Ingrese un número entero de tres dígitos: "))

centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10

for i in range(1, centenas + 1):
    print(i)

for i in range(1, decenas + 1):
    print(i)

for i in range(1, unidades + 1):
    print(i)