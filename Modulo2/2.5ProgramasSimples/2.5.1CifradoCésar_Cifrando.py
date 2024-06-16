"Cada letra del mensaje se reemplaza por su consecuente más cercano"
#A se convierte en B, B se convierte en C y asi sucesivamente
"La única excepción es la Z la cual se convierte en A"

# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
    