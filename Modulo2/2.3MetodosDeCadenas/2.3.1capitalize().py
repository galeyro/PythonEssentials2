"Crea una nueva cadena con la primera letra en mayúscula y el resto en minúsculas"

"La cadena original desde la cual se invoca el método no se cambia de ninguna manera, la inmutabilidad de una cadena se obedece"

"La cadena modificada se devuelve como resultado; si no se usa de alguna manera (asígnala a una variable o pásala a una función/método) desaparecerá sin dejar rastro"

# Demostración del método capitalize():
print('aBcD'.capitalize())
 #Notar que el resto se hizo minusculas
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize()) #Notar que el espacio no se cambio
print('123'.capitalize()) #Notar que los numeros no se cambian
print("αβγδ".capitalize()) #Se convierte A

