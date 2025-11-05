salario = float(input("Salario atual: "))
reajuste = float(input("Percentual do reajuste: "))
salario_reajuste = salario + (salario * (reajuste / 100))
print(f"R${salario_reajuste:.2f}")