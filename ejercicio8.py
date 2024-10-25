# 8. Tabla de Multiplicar
# Genera la tabla de multiplicar de un número dado.

n = int(input("ingresa un numero : "))

print(f"Tabla de multiplicar del {n}")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
