#ENTRADA
info = input("").upper().split(";")
investidor = info[0]
produto = info[1]
aporte_inicial = float(info[2])
aporte_mensal = float(info[3])
meses = int(info[4])
taxa_anual_pct = float(info[5])
taxa_adm_anual_pct = float(info[6])
cashback_pct = float(info[7])

#PROCESSO
taxa_mensal_liquida = ((taxa_anual_pct - taxa_adm_anual_pct) / 12) / 100
fator = (1 + taxa_mensal_liquida) ** meses
serie = ((fator - 1) / taxa_mensal_liquida)
valor_futuro_bruto = aporte_inicial * fator + aporte_mensal * serie
total_aportado = aporte_inicial + aporte_mensal * meses
cashback = total_aportado * (cashback_pct)/100
valor_final = valor_futuro_bruto + cashback
rent_acum_pct = ((valor_final * 100) / total_aportado) - 100

#SAIDA
print(f"RESUMO: {investidor} | PRODUTO: {produto}")
print(f"APORTES: INICIAL=R$ {aporte_inicial:.2f} MENSAL=R$ {aporte_mensal:.2f} MESES={meses}")
print(f"TAXAS: ANUAL={taxa_anual_pct:.2f}% ADM_ANUAL={taxa_adm_anual_pct:.2f}% MENSAL_LIQ={taxa_mensal_liquida * 100:.4f}%")
print(f"TOTAL_APORTADO: R$ {total_aportado:.2f}")
print(f"FV_BRUTO: R$ {valor_futuro_bruto:.2f}")
print(f"CASHBACK: R$ {cashback:.2f}\nVALOR_FINAL: R$ {valor_final:.2f}\nJUROS_GANHOS: R$ {valor_final - total_aportado:.2f}")
print(f"RENT_ACUM_PCT: {round(rent_acum_pct, 2):.2f}%")
