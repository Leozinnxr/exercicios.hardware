n = int(input("Quantos habitantes participarão da pesquisa? "))

soma_salarios = 0
maior_idade = 0
menor_idade = float('inf')
maior_salario = 0
maior_salario_fem = 0
menor_idade_masc = float('inf')
fem_mais_500 = 0
masc_15_50 = 0
idade_18_65_sal_1000 = 0

for i in range(1, n + 1):
    print(f"\nHabitante {i}:")
    idade = int(input("Idade: "))
    sexo = int(input("Sexo (1-Feminino, 2-Masculino): "))
    salario = float(input("Salário: "))

    soma_salarios += salario

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    if salario > maior_salario:
        maior_salario = salario

    if sexo == 1:
        if salario > maior_salario_fem:
            maior_salario_fem = salario
        if salario > 500:
            fem_mais_500 += 1
    elif sexo == 2:
        if idade < menor_idade_masc:
            menor_idade_masc = idade
        if 15 <= idade <= 50:
            masc_15_50 += 1

    if 18 <= idade <= 65 and salario > 1000:
        idade_18_65_sal_1000 += 1

media_salarios = soma_salarios / n

print("\n=== RESULTADOS ===")
print(f"a) Média de salário: R${media_salarios:.2f}")
print(f"b) Maior idade: {maior_idade}")
print(f"c) Menor idade: {menor_idade}")
print(f"d) Maior salário: R${maior_salario:.2f}")
print(f"e) Maior salário do sexo feminino: R${maior_salario_fem:.2f}")
print(f"f) Menor idade do sexo masculino: {menor_idade_masc}")
print(f"g) Mulheres com salário > R$500: {fem_mais_500}")
print(f"h) Homens com idade entre 15 e 50 anos: {masc_15_50}")
print(f"i) Pessoas entre 18 e 65 anos com salário > R$1000: {idade_18_65_sal_1000}")
