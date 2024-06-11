from random import seed, random

seed(0)#Definimos una semilla constante y por eso siempre que ejecutemos el programa da los mismos valores
#Si no definimos una semilla, el valor de la semilla es el tiempo actual
#La semilla recibe un valor int

for i in range(5):
    print(random())#random() produce un numero flotante aleatorio entre 0 y 1