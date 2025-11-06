cot_dolar = float(input("Cotação do dolar: "))
dolar = float(input("Valor para converter para R$: "))

real = dolar * cot_dolar

print(f"R${real:.2f}")