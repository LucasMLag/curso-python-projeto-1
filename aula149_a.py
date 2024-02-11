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



p1 = Pessoa('João',19)


pessoa_p1 = vars(p1)

with open("aula149.json",'w',encoding="utf-8") as arquivo:
    json.dump(
        pessoa_p1,
    arquivo,
      indent=2, 
      ensure_ascii=False

)

print("Pessoa Criada e arquivo salvo!!!")
