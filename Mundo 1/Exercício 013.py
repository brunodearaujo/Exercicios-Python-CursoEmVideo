#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n1 = float(input('Digite seu salário e mostrarei como seria caso tivesse 15% de aumento.'))
print (f'Com aumento de 15%, o seu salário seria: {n1 + (n1 * 15) / 100}R$!')