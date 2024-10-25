# 4. Mayor de Tres Números
# Escribe un programa que encuentre el mayor de tres números dados.

a = float(input("ingresa un numero a : "))
b = float(input("ingresa un numero b : "))
c = float(input("ingresa un numero c : "))


mayor = max(a, b, c)
print(f"El mayor de {a}, {b}, y {c} es {mayor}")