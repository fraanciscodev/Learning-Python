# 27. Determinar Edad
# Calcula la edad de una persona dada su fecha de nacimiento.

from datetime import datetime

fecha_nacimiento = datetime(2002, 12, 3)
hoy = datetime.now()
edad = hoy.year - fecha_nacimiento.year

# Verificar si aún no ha cumplido años este año
if hoy.month < fecha_nacimiento.month or (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
    edad -= 1

print(f"La edad es {edad} años")