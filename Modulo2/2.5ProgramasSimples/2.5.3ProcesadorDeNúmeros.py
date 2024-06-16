"""
Permite ingresar una línea llena de números y sumarlos facilmente

Nota: La función input(), combinada junto con las funciones int() o float(), no es lo adecuado para este propósito
"""
#Procesador de Números.

line = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")
    