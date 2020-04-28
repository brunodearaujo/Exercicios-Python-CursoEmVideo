'''Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input('Digite o seu nome completo: ')).strip()
print(f'Nome em letras minúsculas: {nome.lower()}')
print(f'Nome em letras maiúsculas: {nome.upper()}')
print(f'Primeiro nome tem', nome.find(' '), 'letras.')
print(f'O nome tem',len(nome) - nome.count(' '),'letras no total.')