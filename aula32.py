"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# existe algo sobre funcoes e metodos, que vc esta esquecendo.. hmm o ()? sim, oh, o teclado nao esta igual ao seu Çs esta  heeheu o esqueci OK
# ta confuso esse codigo para mim, muitas validacoes
# bom momento para te explicar os atalhos de identacao do VSCODE,
# seleciona tudo, e ai se vc apertar (tab), vc identa td
# ou, seleciona tudo e ai aperta (shitf+tab), e tira uma identacao de td

print('Programa 1: Par ou Impar\n')

str_numero = input('Digite um número inteiro: ')
if ( not str_numero.isdigit()):
    print("O valor digitado náo é um numero inteiro.")
else:
    int_numero = int(str_numero)
    resto = int_numero % 2
    if (resto == 0):
            print("O número digitado é par.")
    else:
        print("O numero digitado é um número impar.") 

print('') # Quebra de linha

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

print('Programa 2: dia / tarte / noite\n')

# Recendo e validado o valor da hora
horas = input('Que horas são? ')
try:
    horas = int(horas)
except:
    print('O valor das horas precisa ser um numero inteiro.')
    exit()
if horas < 0 or horas > 23:
    print('O valor das horas precisa ser entre 0 e 23.')
    exit()

# Exibindo a mensagem baseado no horario
if horas >= 0 and horas <= 11:
    print(f'Bom dia!')
elif horas >= 12 and horas <= 17:
    print(f'Bom tarde!')
else:
    print(f'Boa noite!')

print('') # Quebra de linha

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

print('Programa 3: Tamanho do nome\n')

nome = input("Digite o seu nome: ")
tamanho = len(nome)
if (tamanho<=4):
    print("Seu nome é curto.")
elif (tamanho>=5) and (tamanho<=6):
    print("Seu nome é normal")
else: 
    print("Seu nome é muito grande")
