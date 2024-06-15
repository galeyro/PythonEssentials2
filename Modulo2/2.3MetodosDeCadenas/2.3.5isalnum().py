"Comprueba si la cadena contiene solo dígitos o caractéres alfabéticos y devuelve True o False según el resultado"

# Demostración del método isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'#tiene espacios
print(t.isalnum())

t = '&Alpha;&beta;&Gamma;&delta;'#tiene caracteres especiales
print(t.isalnum())

t = '20E1'
print(t.isalnum())
