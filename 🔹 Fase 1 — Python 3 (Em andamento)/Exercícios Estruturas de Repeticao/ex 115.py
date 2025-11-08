media_salarial = 0
media_filhos = 0
maior_sal = 0
pessoas_200 = 0
cont_pess = 0
percentual_200 = 0
flag = True

while flag:
    salario = float(input("Salário: "))
    filhos = int(input("Filhos: "))
    cont_pess += 1
    media_salarial += salario
    media_filhos += filhos
    if salario > maior_sal:
        maior_sal = salario
    if salario <= 200:
        pessoas_200 += 1
    opcao = int(input("Deseja continuar o cadastro? 1.Sim 2. Não: "))
    if opcao == 1:
        continue
    else:
        flag = False

media_salarial = media_salarial / cont_pess
media_filhos = media_filhos / cont_pess
percentual_200 = (pessoas_200 * 100) / cont_pess

print(f"A: R${media_salarial:.2f}\nB: {media_filhos}\nC: R${maior_sal:.2f}")
if pessoas_200 > 0:
    print(f"D: {percentual_200:.2f}")
