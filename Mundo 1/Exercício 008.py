#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n1 = float(input('Digite a quantidade de metros: '))
print(f'Fazendo a conversão, {n1} metro(s) é igual a {n1 * 100:.2f} centímetros, e {n1 * 1000:.2f} milímetros.')
