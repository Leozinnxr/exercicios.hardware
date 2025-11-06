salario_min = float(input("Salario minimo: "))
gasto_qw = int(input("Quilowatts gastos: "))

valor_qw = (salario_min / 7) / 100
val_qw_pago = gasto_qw * valor_qw
desconto_qw = val_qw_pago - (val_qw_pago * 0.10)

print(f"Valor do qw: {valor_qw:.2f}\nValor a ser pago: {val_qw_pago:.2f}\nValor com desconto de 10%: {desconto_qw:.2f}")
