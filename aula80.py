# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

num_acertos = 0
opcao_digitada = 0
for pergunta in perguntas:

    # Faz a pergunta
    print(pergunta['Pergunta'])

    # Mostra as opçoes com index
    print('Opções:')
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice}) {opcao}')
    opcao_digitada = input('Escolha uma opção: ')    

    # Testa se o index digitado é o da resposta certa
    try:
        opcao =int(opcao_digitada)
        if pergunta['Opções'][opcao] == pergunta['Resposta']:
            num_acertos += 1
            print('Acertou')
        else:
            print('Errou')
    except:
        print('Errou')

    print('')  # Quebra de linha

# Exibe numero de acertos
print(f'Você acertou {num_acertos} de 3')