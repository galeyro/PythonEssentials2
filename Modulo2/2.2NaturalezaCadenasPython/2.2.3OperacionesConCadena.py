#Funcion ord() devuelve el valor ASCII/UNICODE de un carácter específico

char1='a'
char2=' '
print(ord(char1))
print(ord(char2))

#chr() toma un punto de código y devuelve su carácter correspondiente
print(chr(97))  
print(chr(945))

""""Notar que:
             chr(ord(x)) == x & ord(chr(x)) == x son verdaderos siempre.
"""

