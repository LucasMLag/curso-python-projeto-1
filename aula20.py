# Aula 20: Exercicio If, Elif, Else

numero_1 = input('Digite o primeiro numero: ')
numero_2 = input('Digite o segundo numero: ')

if (numero_1 > numero_2):
    print('O primeiro numero', numero_1, 'é maior que o segundo numero', numero_2)
elif (numero_2 > numero_1):
    print('O segundo numero', numero_2, 'é maior que o primeiro numero', numero_1)
else:
    print('Os numeros sao iguais')