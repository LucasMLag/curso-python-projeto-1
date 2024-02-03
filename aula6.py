# Aula 6: Casting

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool

# str
print('a' + 'b')  # Concatenação (colocar dois textos juntos, não soma. "a" + "b" = "ab")
print(str(1) + '2')  # Transforma o int 1 em uma string '1' e faz concatenação ('1' + '2' = '12')

# int
print(1 + 2)  # Soma (1 + 2 = 3)
print(str('10') + 20)  # Transforma a instring '10' em um int 10 e faz a soma (10 + 20 = 30)

# float
print(float('1') + 2)  # Transforma a string '1' em um float 1.0 e faz a soma com um int sem problemas
# O resultado dessa operação é um float. (1.0 + 2 = 3.0)

# bool
print(bool(''))  # Uma string vazia convertida em bool é False
print(bool(' '))  # Uma string com algo, mesmo um simples espaço, convertida em bool é True