# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

tarefas = []
historico_tarefas = []

while True:

    print('Comandos: listar, desfazer, refazer, sair.')
    entrada = input('Digite uma tarefa ou o comando: ')
    print()

    if (entrada == 'listar'):
        if tarefas:
            print(tarefas)
        else:
            print('Nada para listar.')

    elif (entrada == 'desfazer'):
        if tarefas:
            print(f'Removendo a tarefa "{tarefas[-1]}" da lista.')
            tarefas.pop()
        else:
            print('Nada para desfazer.')

    elif (entrada == 'refazer'):
        if len(historico_tarefas) > len(tarefas):
            print(f'Re-adicionando a tarefa "{historico_tarefas[len(tarefas)]}" na lista.')
            tarefas.append(historico_tarefas[len(tarefas)])
        else:
            print('Nada para refazer.')
       
    elif (entrada == 'sair'):
        print('Saindo.')
        break

    else:
        print(f'{entrada} foi adicionado a lista de tarefas.')
        tarefas.append(entrada)
        historico_tarefas = tarefas

    print()
