#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Qual o nome da sua cidade natal? ')).strip().lower()
print(cidade[:5] == 'santo')
