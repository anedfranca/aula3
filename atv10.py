#Crie um programa que exiba os itens exclusivos de dois
#dicionários. Itens exclusivos são aqueles que não estão
#presentes em ambos os dicionários.
pessoas = {
    'maria':20,    'pedro':40,    'epaminondas':80
}

alunos = {
    'juliana':25,    'pedro':40,    'helena':30
}
resposta = {}

for item in pessoas.items():
    if item not in alunos.items():
        resposta[item[0]] = item[1]
        
for item in alunos.items():
    if item not in pessoas.items():
        resposta[item[0]] = item[1]
        
print(resposta)