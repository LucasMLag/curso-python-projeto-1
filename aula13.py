# Aula 13: Introdução a f-strings

nome = 'João'
altura = 1.80
peso = 95
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# João tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

nome = 'Joao'
idade = 17
ano = 2023-idade
carteira = 17.40

linha_1 = f'O {nome} tem {idade} anos e nasceu '
linha_2 = f'em {ano} e recebeu {carteira:.4f}'
print(linha_1)
print(linha_2)