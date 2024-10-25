# 18. Números Fibonacci
# Genera la serie de Fibonacci hasta un número n dado.

n = 43
a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b

