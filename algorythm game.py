import math
def dziesietny_do_binarnego(dziesietna_liczba_mniejsza_od_2_do_20):
    var = dziesietna_liczba_mniejsza_od_2_do_20
    lista = []
    lista_all = []
    for i in range(20, -1, -1):
        lista_all.append(2**i)
    double = ''

    while True:
        if var == 0:
            break
        for i in range(20, -1, -1):
            kwadrat = 2**i
            if kwadrat > var:
                pass
            else:
                var -= kwadrat

                lista.append(kwadrat)
    for i in lista_all:
        if i in lista:
            double += '1'
        else:
            if len(double) == 0:
                pass
            else:
                double += '0'
    return double
num_1 = int(input('choose a number between 1 and 1430: '))
num_2 = int(input('choose a number between 1 and 1430: '))
value = 0
if num_1 > 1430 or num_1 < 1 or num_2 > 1430 or num_2 < 1:
    print('the numbers is not correct')
else:
    if num_1 > num_2:
        for i in range(num_2, num_1+1, 2):
            value += i
            print(i)
    elif num_2 > num_1:
        for i in range(num_1, num_2+1, 2):
            value += i
            print(i)
    else:
        for i in range(num_1+1, 2):
            value += i
print('suma=', value)
print(dziesietny_do_binarnego(value))


