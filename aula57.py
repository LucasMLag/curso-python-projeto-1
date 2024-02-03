#Exercicio
# oi? tgm
lista_compras = []
while True:
    opcao = input('[i] inserir, [a] apagar [l] lista ')
    if opcao.lower() == 'i':
        lista_compras.append(input('Digite qual item você quer adicionar na lista '))
    if opcao.lower() == 'a':
        indice = int(input('Qual o indice do item você quer apagar? '))
        if len(lista_compras) > indice:
            lista_compras.pop(indice)
        else:
            print('Houve um erro - O indice que você tentou apagar não existe!!!')
            continue
    if opcao.lower() == 'l':
        if len(lista_compras) <= 0:
            print('A lista esta vazia')
        else:
            for item in enumerate(lista_compras):
                print(item)
    

