from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0)) #Fijate que usas logaritmo base e de e y eso es igual a 1

