# 30. Divisores de un Número
# Encuentra todos los divisores de un número dado.

numero = int(input("ingresa una numero cualquiera : "))
divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print(f"Los divisores de {numero} son: {divisores}")