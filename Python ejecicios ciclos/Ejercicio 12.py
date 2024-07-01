numero = int(input("Ingrese un número entero de tres dígitos: "))

centenas = numero // 100
decenas = (numero % 100) // 10
unidades = numero % 10

tiene_uno = False
if centenas == 1 or decenas == 1 or unidades == 1:
    tiene_uno = True

if tiene_uno:
    print("El número tiene el dígito 1.")
else:
    print("El número no tiene el dígito 1.")