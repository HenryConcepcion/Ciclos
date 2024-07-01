numero = int(input("Ingrese un número entero: "))

suma_factoriales = 0
for i in range(1, numero + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j

    suma_factoriales += factorial

print("La sumatoria de las factoriales de los números entre 1 y", numero, "es:", suma_factoriales)