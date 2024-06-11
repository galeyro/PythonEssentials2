from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar) #deja de ser tipo int

print(ad == 90.) #True
print(ar == pi / 2.) #True  #importado de math
print(sin(ar) / cos(ar) == tan(ar)) #True propiedad trigonométrica
print(asin(sin(ar)) == ar) #True propiedad función inversa