"""
La comparación está estrechamente relacionada con el ordenamiento (o más bien, el ordenamiento es, de hecho, un caso muy sofisticado de comparación).

Esta es una buena oportunidad para mostrar dos formas posibles de ordenar listas que contienen cadenas. Dicha operación es muy común en el mundo real: cada vez que ves una lista de nombres, productos, títulos o ciudades, esperas que este ordenada."""

# Demostración de la función sorted():
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)#sorted crea una nueva lista, manteniumdo la original intacta

print(first_greek)
print(first_greek_2)

print()

#El segundo método afecta a la lista misma, no se crea una nueva lista. El ordenamiento se realiza por el método denominado sort().
# Demostración del método sort():
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
    
