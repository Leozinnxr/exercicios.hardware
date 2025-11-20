valor_parcela = None
valor_total = 0

carro = float(input("Digite o valor do carro: "))

print("""
Quantidade de parcelas    Percentual de acréscimo
        6                            3%
        12                           6%
        18                           9%
        24                           12%
        36                           18%
        48                           24%
        60                           30%""")
qnt_parcelas = {
    6: 0.03,
    12: 0.06,
    18: 0.09,
    24: 0.12,
    36: 0.18,
    48: 0.24,
    60: 0.30,
}
parcelas = int(input("Digite o número de parcelas: "))

if parcelas == 1:
    valor_parcela = carro * 0.20
    valor_total = carro - valor_parcela
elif parcelas not in qnt_parcelas:
    raise ValueError
else:
    for i in qnt_parcelas:
        if i == parcelas:
            valor_parcela = carro * qnt_parcelas[i]
    valor_total = carro + valor_parcela

print(f"Valor total do carro: R${valor_total:.2f}  Valor da parcela: R${valor_total/parcelas:.2f}  Quantidade de parcelas: {parcelas}x")


