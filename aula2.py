# Aula 2: Função print

print(1) # exibe na tela o numero 1, e também quebra a linha no final por padrão

print(1, 2, 3) # exibe na tela os 3 argumentos não nomeados, separando eles com um espaço por padrão, e quebra a linha

print(4, 5, 6, sep='-') # argumento nomeado sep troca o separador padrão ' ' por '-'

print(7, 8, 9, end='.\n') # argumento nomeado end troca o que o print faz no final de cada linha, nesse caso adiciona um ponto final e depois quebra a linha

print(10, 20, 30, sep=', ', end='.\n') # é possivel passar multiplos argumentos nomeados diferentes


# Quebras de linha:
# \r\n -> CRLF (windows)
# \n -> LF (unix, também funciona em windows atuais)