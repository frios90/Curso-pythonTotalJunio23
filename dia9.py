from collections import Counter
from collections import defaultdict


## Para contar elementos repetidos en una lista, array o string
frase = "Esta es una frase de la cual quiero saber cuantas veces se repite cada letra de la misma"

conteo = Counter(frase)

print(conteo)

frase_split = frase.split()
conte_split = Counter(frase_split)

print(conte_split)
print(conte_split.most_common())
print(conte_split.popitem())

## Para setear un valor por defecto al momento de consultar sobre un valor que no existe en un diccionario

mi_dict =  defaultdict(lambda: "este valor es nulo")
mi_dict["uno"] = "algo"

print(mi_dict)
print(mi_dict["dos"])
print(mi_dict)
