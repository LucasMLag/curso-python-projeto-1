# Aula 11: Precedencia

# 1. (n + n)     <- parenteses
# 2. **          <- potencia
# 3. * / // %    <- multiplicaçoes, divisoes
# 4. + -         <- soma, subtraçao

# em caso de operaçoes com mesmo nivel de precedencia as contas são feitas da esquerda para direita, ex.:
conta_1 = 2 * 3 / 5
# primeiro sera realizada a multiplicação, e de pois a divisão

conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_2)