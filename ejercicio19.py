# 19. Número Capicúa
# Verifica si un número es capicúa (se lee igual al derecho y al revés).

numero = int(input("ingresa una numero cualquiera : "))
numero_str = str(numero)

if numero_str == numero_str[::-1]:
    print(f"{numero} es un número capicúa")
else:
    print(f"{numero} no es un número capicúa")