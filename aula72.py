def multiplicao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def par_ou_impar(num):
    res_par_ou_impar = ''
    if num % 2 == 0:
        res_par_ou_impar = f'O número {num} é par.'
    else:
         res_par_ou_impar = f'O número {num} é impar.'
    return res_par_ou_impar

resultado = multiplicao(1,2,3,4,5)
print(resultado)
res = par_ou_impar(2)
print(res)
res = par_ou_impar(3)
print(res)