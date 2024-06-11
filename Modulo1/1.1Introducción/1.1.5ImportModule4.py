from math import sin, pi

print(sin(pi/2))

pi = 3.14

def sin(x): #Reescribes el codigo de la funcion sin
    if 2*x==pi:
        return 0.99999999
    else:
        return None 
    
print(sin(pi/2))