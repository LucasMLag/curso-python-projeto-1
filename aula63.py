# Exercicio validação de cpf

cpf = input('Digite um cpf para validação: ')
resultado = 0
primeiro_digito = 0
segundo_digito = 0

# CPF Valido:
if len(cpf) == 14:

    # Validando o primeiro digito:
    multiplicador = 10
    for char in cpf:
        if char.isdigit():
            numero = int(char)
            resultado += multiplicador * numero
            multiplicador -= 1
            if multiplicador == 1:
                break
    resultado = resultado * 10
    resultado = resultado % 11
    if (resultado > 9):
        primeiro_digito = 0
    else:
        primeiro_digito = resultado
    print(f'`O primeiro digito é {primeiro_digito}')

    # Validando o segundo digito:
    multiplicador = 11
    resultado = 0
    for char in cpf:
        if char.isdigit():
            numero = int(char)
            resultado += multiplicador * numero
            multiplicador -= 1
            if multiplicador == 1:
                break
    resultado = resultado * 10
    resultado = resultado % 11
    if (resultado > 9):
        segundo_digito = 0
    else:
        segundo_digito = resultado
    print(f'`O segundo digito é {segundo_digito}')
    digitos = cpf[12:]
    print(digitos)
    if str(primeiro_digito) == cpf[12:13] and str(segundo_digito) == cpf[13:14]:
       print('Esse cpf é valido') 
    else:
        print('Esse cpf é invalido')

# CPF Invalido:
else:
    print('CPF Invalido')
