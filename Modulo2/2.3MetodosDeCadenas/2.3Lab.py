"""
Ya conoces como funiona el método split(). Ahora queremos que lo pruebes.

Tu tarea es escribir tu propia función, que se comporte casi como el método original split(), por ejemplo:

Debe aceptar únicamente un argumento: una cadena.
Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los lugares donde la cadena contiene espacios en blanco.
Si la cadena está vacía, la función debería devolver una lista vacía.
Su nombre debe ser mysplit().
Utiliza la plantilla en el editor. Prueba tu código con cuidado.
"""
#Plantilla-------------------------------------
def mysplit(strng):
    #strng es mi string que está compuesto por caractéres
    #Utilizaremos el codigo ASCII junto con una lista para identificar que elemento está en la cadena
    #el caracter espacio es el codigo ASCII 32

    my_list = []#lista vacia para guardar los elementos de la cadena
    temp = [] #lista temporal para guardar las variables
    for i in strng:
        if ord(i) != 32:#si no encontramos un caracter de espacio
            temp.append(i)#vamos a guardar el caracter en la lista temporal
        elif ord(i) == 32 :#si encontramos un caracter de espacio
            my_list.append("".join(temp))#guardamos el elemento en la lista principal
            temp = []#limpiamos la lista temporal
    my_list.append("".join(temp))#agregamos el ultimo elemento a la lista temporal

    #comprobamos si la lista es vacia
    boolVacia = True#la lista es vacia
    for i in my_list:
        if i != '':#si encontramos un elemento en la lista 
            boolVacia = False#la lista no es vacia
            break#salimos del ciclo

    if boolVacia:
        lista_vacia=[""]#lista vacia con un elemento
        print(lista_vacia)#mostramos una lista vacia tal como pide la funcion
    else:
        for i in my_list:
            if i == '':
                my_list.remove(i)#removemos los elementos vacios de la lista
        print(my_list)#mostramos en pantalla la lista
    

#Pruebas-----------------------------------------
mysplit("Ser o no ser, esa es la cuestión")
print("\n")
mysplit("Ser o no ser, esa es la cuestión")
print("\n")
mysplit("   ")
print("\n")
mysplit(" abc ")
print("\n")
mysplit("")
    