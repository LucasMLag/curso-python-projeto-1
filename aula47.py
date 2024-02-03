palavra_secreta = "perfume"
palavra_formatada = ""
tentativas = 0
palavra_formatada = '*' * len(palavra_secreta)
while True:
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        continue

    if letra in palavra_secreta:
        index = 0
        while (index < len(palavra_secreta)):
            if palavra_secreta[index] == letra:
                palavra_formatada = palavra_formatada[:index] + letra + palavra_formatada[index+1:]
            index += 1
    tentativas = tentativas+1
    print(palavra_formatada)
    if palavra_secreta == palavra_formatada:
        print(f'Você conseguiu com {tentativas=}') 
        palavra_formatada = '*' * len(palavra_secreta)
        tentativas = 0
    

