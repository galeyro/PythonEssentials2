#Necesitamos 3 ' para poder hacer las cadenas multilinea de manera correcta

multiline = '''Línea #1
Línea #2'''

print(len(multiline))

"""
Notar que en caso de tener:

    multiline = 'nLínea #1
    Línea #2'

Se obtendría un error de sintaxis, ya que no se puede tener un salto de línea en una cadena de texto de una sola línea.
"""

"Las cadenas multilínea también pueden ser creadas con comillas triples"

multiline = """Línea #1
Línea #2"""
print(len(multiline))