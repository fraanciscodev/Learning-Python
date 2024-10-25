# 6. Factorial de un Número
# Calcula el factorial de un número dado.

n = int(input("ingresa un numero : "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    

print(f"El factorial de {n} es {factorial}")