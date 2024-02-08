# Exercício - Adiando execução de funções
def criar_soma(x):
    def soma(y):
        return x + y
    return soma


def cria_multiplica(x):
    def multplica(y):
        return x * y
    return multplica


soma_com_cinco = criar_soma(5)
multiplica_por_dez = cria_multiplica(10)

print(soma_com_cinco(5))
print(multiplica_por_dez(10))