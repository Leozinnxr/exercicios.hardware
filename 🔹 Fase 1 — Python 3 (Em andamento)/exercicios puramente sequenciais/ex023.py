algoritmo_prova = float(input("Algor. prova: "))
algoritmo_trab = float(input("Algor. trab: "))
logpro_prova = float(input("log. programação prova: "))
logpro_trab = float(input("log. programação trab: "))

med_prova = (algoritmo_prova + logpro_prova) / 2
med_trab = (algoritmo_trab + logpro_trab) / 2

nota_final = (med_prova) * 0.6 + (med_trab) * 0.4

print(f"Nota: {nota_final:.2f}")