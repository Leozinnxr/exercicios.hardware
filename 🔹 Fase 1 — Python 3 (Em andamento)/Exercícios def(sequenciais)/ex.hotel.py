#ENTRADA
info = input().upper()
rel = info.split(';')
hotel = rel[0]
quartos_totais = int(rel[1])
dias = int(rel[2])
diarias_vendidas = int(rel[3])
tarifa_base = float(rel[4])
promocao_pct = float(rel[5])
custo_fixo_mensal = float(rel[6])
custo_var_por_diaria = float(rel[7])
high_occ = False
low_occ = False
tarifa_promo = 0

#PROCESSO
diarias_disp = quartos_totais * dias
taxa_ocupacap = (diarias_vendidas / diarias_disp) * 100
if taxa_ocupacap < 40:
    tarifa_promo = tarifa_base * 0.10
    tarifa_final = tarifa_base - tarifa_promo
    low_occ = True
elif taxa_ocupacap > 85:
    tarifa_promo = tarifa_base * 0.05
    tarifa_final = tarifa_base + tarifa_promo
    high_occ = True

tarifa_promo = tarifa_promo + (tarifa_base * promocao_pct/100)
tarifa_final = tarifa_base - tarifa_promo
receita = float(diarias_vendidas * tarifa_final)
custo_tot = custo_fixo_mensal + custo_var_por_diaria * diarias_vendidas
revpar = receita / diarias_vendidas
resultado_mes = receita - custo_tot
if resultado_mes < 0:
    resultado = "PREJUIZO"
elif resultado_mes > 0:
    resultado = "LUCRO"
else:
    resultado = "EQUILIBRIO"

def real(valor):
    valor = f"{valor:,.2f}"
    valor = valor.replace('.', 'v').replace(',', '.').replace('v', ',')
    return valor

#SAIDA
print(f"RESUMO: {hotel.title()}")
print(f"ESTOQUE: QUARTOS={quartos_totais} DIAS={dias} DIARIAS_DISPONIVEIS=")
print(f"OCUPACAO_PCT: {taxa_ocupacap:.2f}%")
print(f"TARIFAS: BASE=R$ {real(tarifa_base)} PROMO=R${real(tarifa_promo)} FINAL=R${real(tarifa_final)}")
print(f"AJUSTES_AUTO: LOW_OCC(-10%)={low_occ} HIGH_OCC(+5%)={high_occ}")
print(f"RECEITA: R${real(receita)}\nCUSTO_TOTAL: R$ {real(custo_tot)}\nREVPAR: R${real(revpar)}")
print(f"RESULTADO_TIPO: {resultado}\nLUCRO_PREJUIZO: R$ {real(resultado_mes)}")
