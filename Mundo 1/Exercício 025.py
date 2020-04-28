#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite o seu nome completo: ')).strip().lower()
silva = bool(nome.split().count('silva'))
print(f'O seu nome tem "Silva" ? {silva}')