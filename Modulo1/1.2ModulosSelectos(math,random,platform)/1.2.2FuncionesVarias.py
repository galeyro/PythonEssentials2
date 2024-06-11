from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y)) #entero más grande menor o igual a x
print(floor(-x), floor(-y)) #entero más grande menor o igual a x
print(ceil(x), ceil(y)) #entero más pequeño mayor o igual a x
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y)) #trunca el valor a un entero cortando su parte decimal
print(trunc(-x), trunc(-y)) #trunca el valor a un entero cortando su parte decimal
    