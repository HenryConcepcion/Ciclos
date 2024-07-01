x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))

suma_multiplos_2 = 0
for i in range(1, x + 1):
    suma_multiplos_2 += i * 2

promedio_multiplos_2 = suma_multiplos_2 / x

suma_multiplos_5 = 0
for i in range(1, y + 1):
    suma_multiplos_5 += i * 5

promedio_multiplos_5 = suma_multiplos_5 / y

if promedio_multiplos_2 > promedio_multiplos_5:
    print("El promedio de los", x, "primeros múltiplos de 2 es mayor que el promedio de los", y, "primeros múltiplos de 5.")
else:
    print("El promedio de los", x, "primeros múltiplos de 2 no es mayor que el promedio de los", y, "primeros múltiplos de 5.")