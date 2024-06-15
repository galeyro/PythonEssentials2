"Similar al metodo index(), busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero si no se encuentra, en lugar de generar una excepción, devuelve -1"

"Funciona solo con cadenas"

# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))
#si deseas realizar la búsqueda, no desde el principio sino desde otra posición, usamos la variante con dos parámetros
print("\n\n")
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)
    