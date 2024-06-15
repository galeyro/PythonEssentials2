"""
Hay dos cuestiones adicionales que deberían discutirse aquí: ¿Cómo convertir un número (un entero o un flotante) en una cadena, y viceversa? Puede ser necesario realizar tal transformación. Además, es una forma rutinaria de procesar datos de entrada o salida.

La conversión de cadena a número es simple, ya que siempre es posible. Se realiza mediante una función llamada str().
"""

itg = 13
flt = 1.3
#conviertes en cadenas
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)
    
"""
La transformación inversa solo es posible cuando la cadena representa un número válido. Si no se cumple la condición, espera una excepción ValueError.

Emplea la función int() si deseas obtener un entero, y float() si necesitas un valor punto flotante.
"""

si = '13'
sf = '1.3'
itg = int(si)#conviertes en entero
flt = float(sf)#conviertes en flotante

print(itg + flt)
    