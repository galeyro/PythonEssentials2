"""
Inmutabilidad: No puedes cambiar una cadena después de crearla. No puedes usar métodos como append() o insert() en cadenas.
Eliminar cadenas: Solo puedes eliminar una cadena completa, no parte de ella.
"""
#No pienses que la inmutabilidad de una cadena limita tu capacidad de operar con ellas.
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet #agrega a al principio de la cadena (concatenación)
alphabet = alphabet + "z" #agrega z al final de la cadena (concatenación)

print(alphabet) #abcdefghijklmnopqrstuvwxyz
