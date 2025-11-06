salario = float(input("Salario: "))
prestacao = float(input("Prestação: "))
prestacao_max = salario * 0.30

if prestacao <= prestacao_max:
    print("Prestação aprovada!")
else:
    print("Prestação indisponivel!")
    