pi = 3.14

def sin(x): 
    if 2*x==pi:
        return 0.99999999
    else:
        return None
    
print(sin(pi/2))

from math import sin, pi#importas el modulo math y la función se queda con la del modulo y no la definida por nosotros

print(sin(pi/2))