# 24. Suma de Dígitos
# Suma todos los dígitos de un número.

numero = 1234
suma_digitos = sum(int(digito) for digito in str(numero))

print(f"La suma de los dígitos de {numero} es {suma_digitos}")

