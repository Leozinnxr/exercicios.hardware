cont_par = 0
cont_impar = 0
for cont in range(0, 3, +1):
    n = int(input())

    if n % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print(cont_impar, cont_par)