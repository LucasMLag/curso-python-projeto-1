# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def decoradora(func):
    ...

lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']


def junta_listas(lista_1,lista_2):

    lista_final = []

    if len(lista_1) <= len(lista_2):
        iterator = iter(lista_2)
        for item in lista_1:
            lista_final.append((item, next(iterator)))
    else:
        iterator = iter(lista_1)
        for item in lista_2:
            lista_final.append((item, next(iterator)))
    
    return lista_final

print(junta_listas(lista_1, lista_2))
