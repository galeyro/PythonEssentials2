#in: Verifica si una cadena está dentro de otra ('Py' in 'Python' da True).
#not in: Verifica si una cadena no está dentro de otra ('Java' not in 'Python' da True).
print("In--------------\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet) #si está
print("F" in alphabet) #no está (MAYUSCULA)
print("1" in alphabet) #no está (número)
print("ghi" in alphabet)  #si está
print("Xyz" in alphabet) #no está (MAYUSCULA)
print("bcn" in alphabet) #no está (no está en orden)

print("\nNot it--------------\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)
print("bcn" not in alphabet)
