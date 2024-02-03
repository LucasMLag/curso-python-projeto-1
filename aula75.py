# multiplicao

def criar_multiplicacao(qntd):
    def multiplicar(numero):
        return numero * qntd
    return multiplicar

duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

print(f'O dobro de 12 é {duplicar(12)}' )
print(f'O dobro de 3 é {duplicar(3)}')
print(f'O triplo de 9 é {triplicar(9)}')
print(f'O quadruplo de 3 é {quadruplicar(3)}')







