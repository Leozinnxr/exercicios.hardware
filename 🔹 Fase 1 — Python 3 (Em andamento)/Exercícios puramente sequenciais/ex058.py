comprimento_pista = float(input("Comprimento da pista (em metros): "))
total_voltas = int(input("Total de voltas: "))
reabastecimentos = int(input("Número de reabastecimentos: "))
consumo = float(input("Consumo (em km/L): "))

comprimento_km = comprimento_pista / 1000
voltas_por_abastecimento = total_voltas / (reabastecimentos + 1)
distancia = voltas_por_abastecimento * comprimento_km
litros = distancia / consumo

print(f"Litros necessários até o primeiro reabastecimento: {litros:.2f}L")
