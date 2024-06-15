"Genera una copia de la cadena original, tratando de centrarla dentro de un campo de ancho especificado"

# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
#center(10) significa que la cadena debe centrarse en un campo de 10 caracteres de ancho

print('[' + 'Beta'.center(2) + ']')#Si la longitud del campo es menor que la longitud de la cadena, la cadena se devuelve sin cambios
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(20, '*') + ']')#La variante de dos parámetros de center() hace uso del carácter del segundo argumento, en lugar de un espacio en blanco