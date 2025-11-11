tot_avista = 0
tot_prazo = 0
tot_compras = 0
cont_prazo = 0
pri_prest = 0

for cont in range(1, 16):
    valor = float(input("Valor de compra: R$"))
    tipo = input("A Prazo(P) ou à Vista(V): ").upper()
    tot_compras += valor

    if tipo == "V":
        tot_avista += valor
    elif tipo == "P": 
        if cont_prazo == 1:
            continue
        else:
            pri_prest = valor / 3
            cont_prazo = 1
        tot_prazo += valor
    valor = 0
    tipo = 0
    
print(f"""o valor total das compras à vista: R${tot_avista:.2f}
o valor total das compras a prazo: R${tot_prazo:.2f}
o valor total das compras efetuadas na loja: R${tot_compras:.2f}
o valor da primeira prestação das compras a prazo, sabendo que essas serão pagas em 3
vezes: R${pri_prest:.2f}""")
