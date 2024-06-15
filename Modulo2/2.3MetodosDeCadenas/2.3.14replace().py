"devuelve una copia de la cadena original en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento"

# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))#reemplaza dos veces ojo
print("Apple juice".replace("juice", ""))

"La variante del método replace() con tres parámetros emplea un tercer argumento (un número entero) que limita el número de reemplazos que se pueden realizar:"

print("This is it!".replace("is", "are", 1))#reemplaza una vez
print("This is it!".replace("is", "are", 2))