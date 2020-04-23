#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import floor
n = float(input('Digite um número real: '))
n = floor(n)
print(f'A parte inteira desse número é {n}')