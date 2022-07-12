#Aprovechando la función del profesor
from operaciones import es_primo

lista =  [3, 4, 8, 5, 5, 22, 13]

num_primos = list(filter(es_primo ,lista))
print(num_primos)
