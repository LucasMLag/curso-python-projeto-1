"""
Iterando strings com while
"""

# Exercicio, fazer um programa que le um nome e faz o nome ter asteriscos em volta de cada letra

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
resultado = ''
num_letra = 0

while (num_letra < tamanho_nome):
    resultado += '*'
    resultado += nome[num_letra] 
    num_letra += 1
print(resultado)