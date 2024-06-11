#Platform devuelve una cadena que describe el entorno de ejecución de Python.
from platform import platform

print(platform()) #Devuelve la plataforma en la que se está ejecutando Python.
print(platform(1))#acepta un argumento aliased. Si el argumento es true, devuelve una cadena que describe la plataforma en un conocido
print(platform(0,1))#acepta un argumento terse. Si el argumento es true, devuelve una cadena corta que describe la plataforma en un formato simple.
