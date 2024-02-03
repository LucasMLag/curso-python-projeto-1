# Aula 14: Introdução a .format

a = 'A'
b = 'B'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

# Outros exemplos:

# args, forma automatica
exemplo_1 = '{} {} {}'.format('A', 'B', 'C') 
print(exemplo_1)  # A B C

# args, forma manual
exemplo_2 = '{2} {1} {1}'.format('A', 'B', 'C')
print(exemplo_2)  # C B B

# kwargs
exemplo_3 = '{arg2} {arg3} {arg1}'.format(arg1='A', arg2='B', arg3='C')
print(exemplo_3)  # B C A

# args e kwargs, forma automatica
exemplo_4 = '{meu_kwarg} {} {}'.format('A', 'B', meu_kwarg='C')
print(exemplo_4)  # C A B

# args e kwargs, forma manual
exemplo_5 = '{meu_kwarg} {1} {0}'.format('A', 'B', meu_kwarg='C')
print(exemplo_5)  # C B A
