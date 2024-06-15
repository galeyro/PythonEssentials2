"""
Ya conoces como funiona el método split(). Ahora queremos que lo pruebes.

Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

Debe aceptar únicamente un argumento: una cadena.
Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
Si la cadena está vacía, la función debería devolver una lista vacía.
Su nombre debe ser mysplit().
Utiliza la plantilla en el editor. Prueba tu código con cuidado.
"""

def mysplit(strng):
    #strng es mi string que está compuesto por caractéres
    #Utilizaremos el codigo ASCII junto con una lista para identificar que elemento está en la cadena
    #el caracter espacio es el codigo ASCII 32

    my_list = []#lista vacia para guardar los elementos de la cadena
    temp = [] #lista temporal para guardar las variables
    for i in strng:
        if ord(i) != 32:
            temp.append(i)
        elif ord(i) == 32:
            my_list.append("".join(temp))
            temp = []#limpiamos la lista temporal

    #mostramos en pantalla la lista
    print(my_list)



print(mysplit("Ser o no ser, esa es la cuestión"))
print("\n\n")
print(mysplit("Ser o no ser, esa es la cuestión"))
print("\n\n")
print(mysplit("   "))
print("\n\n")
print(mysplit(" abc "))
print("\n\n")
print(mysplit(""))
    