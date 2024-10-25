# 11. Contador de Vocales
# Cuenta el número de vocales en una cadena de texto.

cadena = (input("ingresa una palabra o frase : "))
vocales = "aeiouáéíóú"
contador = 0

for letra in cadena.lower():
    if letra in vocales:
        contador += 1

print(f"La cadena tiene {contador} vocales")
