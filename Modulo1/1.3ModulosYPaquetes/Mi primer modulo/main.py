from sys import path

path.append('..∖∖modules')

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))



""" 
En caso de tener el modulo en una carpeta diferente, debemos importar el path

import sys
for p in sys.path:
    print(p)
"""