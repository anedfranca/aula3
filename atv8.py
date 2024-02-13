#Escreva um programa que percorra um dicionário
#contendo informações de pessoas (nome, idade) e exiba essas informações.

pessoas1 = {
    'maria':20,
    'pedro':40,
    'epaminondas':80
}
print(pessoas1['maria'])

pessoas2 = {
    'pessoa1':['maria',20],
    'pessoa2':['pedro',40],
    'pessoa3':['epaminondas',80]
}
print(pessoas2['pessoa3'][1])

pessoas3 = {
    'pessoa1':{'nome':'maria','idade':20},
    'pessoa2':{'nome':'pedro','idade':40},
    'pessoa3':{'nome':'epaminondas','idade':80}
}
print(pessoas3['pessoa1']['idade'])