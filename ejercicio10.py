# 10. Palíndromo
# Verifica si una palabra o frase es un palíndromo.

cadena = "anita lava la tina"
cadena = cadena.replace(" ", "").lower()

if cadena == cadena[::-1]:
    print(f"'{cadena}' es un palíndromo")
else:
    print(f"'{cadena}' no es un palíndromo")
