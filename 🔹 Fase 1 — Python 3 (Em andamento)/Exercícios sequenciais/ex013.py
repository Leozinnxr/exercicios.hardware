valor_hr = int(input("Valor por hora: "))
hrs_trab = int(input("Horas Trab: "))
bruto = valor_hr * hrs_trab
imposto = 0.11 * bruto
inss = 0.08 * bruto
sindicato = 0.05 * bruto
liquido = bruto - (imposto + inss + sindicato)

print(f"Bruto: {bruto}  Liquido: {liquido}\n INSS: {inss}  Imp. de renda: {imposto}  Sindicato: {sindicato}")