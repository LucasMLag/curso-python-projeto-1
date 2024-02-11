# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
class Pessoa:
    def __init__ (self,nome,idade):
        self.nome = nome
        self.idade = idade



p1 = Pessoa('1','1')
try:
    with open("aula149.json",'r',encoding='utf-8') as arquivo:
        p1.__dict__ = (json.load(arquivo))
except:
    print('Arquivo não localizado')

print('Nome ',p1.nome)
print('Idade ',p1.idade)