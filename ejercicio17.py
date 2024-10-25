# 17. Múltiplos de 3 y 5
# Imprime todos los múltiplos de 3 y 5 entre 1 y 100.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
