#Escreva um programa que receba duas listas e calcule
#a união dos elementos únicos dessas listas, usando conjuntos.

a = [1,2,3,4,5]
b = [99,88,2,77,66,4]

resposta = set(a).union(set(b))

print(resposta)