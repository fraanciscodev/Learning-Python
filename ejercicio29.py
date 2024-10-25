# 29. Conteo Regresivo
# Crea un contador que cuente hacia atrás desde un número n hasta 0.

n = int(input("ingresa una numero cualquiera : "))

for i in range(n, -1, -1):
    print(i)