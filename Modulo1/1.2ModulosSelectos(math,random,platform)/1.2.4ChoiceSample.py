from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#sample selecciona un número de elementos de una lista. Es util cuando necesitas elementos aleatorios de una muestra sin reemplazo, es decir, cada elemento es único y no se repite.

print(choice(my_list))#solo un elemento
print(sample(my_list, 5))#5 elementos
print(sample(my_list, 10))#10 elementos
