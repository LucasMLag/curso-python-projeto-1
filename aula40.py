"""
Cauculadora com while


"""
while True:
    sair = input("Quer sair? [S]im ou [N]ão: ")
    if (sair == 'N') or (sair == "n"):
        print("Você digitou N ou n")
    elif (sair == 'S') or (sair == 's'):
        break
    else:
        print('Você digitou uma opção errada!!!')
        continue

    # Lê e valida o tipo de operação
    tipo = None
    while tipo != '+' and  tipo != '-' and tipo != '*' and tipo != '/':
        if tipo != None and tipo != '+' and  tipo != '-' and tipo != '*' and tipo != '/':
            print('Erro: Tipo invalido! (+,-,*,/)')
        tipo = input('Qual operação você quer fazer? ')

    # Lê e valida o primeiro número
    str_num_1 = input('Digite o primeiro número: ')
    try: 
        int_num1 = float(str_num_1)
    except:
        print('Erro: Número Invalido')
        quit()

    # Lê e valida o segundo número
    str_num_2 = input('Digite o segundo número: ')
    try: 
        int_num2 = float(str_num_2)
    except:
        print('Erro: Número Invalido')
        quit()
    
    if (tipo == '+'):
        resultado = int_num1 + int_num2
    elif (tipo == '-'):
        resultado = int_num1 - int_num2
    elif (tipo == '*'):
        resultado = int_num1 * int_num2
    elif (tipo == '/'):
        resultado = int_num1 / int_num2
    else:
        print('Tipo de operação não reconhecida')
        continue
    print("Resultado da conta: ", resultado)
    
    # ~e vc rolando para cima, nem tava com a mao no teclado nem mouse
    # to pronto oi 