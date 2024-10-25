# 7. Número Primo
# Verifica si un número es primo.

numero = int(input("ingresa un numero : "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")

