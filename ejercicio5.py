# 5. Suma de Números en un Rango
# Calcula la suma de todos los números del 1 al 100.

suma = sum(range(1, 101))
print(f"La suma de los números del 1 al 100 es {suma}")

# en este caso nos daría una leve variación de la suma, pues considerará la suma de 99 números
suma = sum(range(1, 100))
print(f"La suma de los números del 1 al 100 es {suma}")