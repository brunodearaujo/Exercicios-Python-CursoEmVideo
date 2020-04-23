#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
janela = float (input('Caso tenha janelas ou portas, some das janelas e portas e coloque aqui, caso não tenha digite 0. '))
c = (largura + altura - janela) / (2**2)
print(f'Você precisará de {c} litros de tinta.')