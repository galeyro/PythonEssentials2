"hacen casi lo mismo que sus contrapartes que no tienen el prefijo r, pero comienzan a buscar desde el final de la cadena, no desde el principio."

# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))#empieza a buscar desde la posición 9 la cual es la última 'a' y como no hay más 'ta' devuelve -1
print("tau tau tau".rfind("ta", 3, 9))#busca desde la posición 3 hasta la 9, devuelve 4 porque es la posición de la primera 'ta' que encuentra
    