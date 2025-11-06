eleitores = int(input("Eleitores: "))
vt_branco = int(input("Voto em branco: "))
vt_nulo = int(input("Voto nulo: "))
vt_valido = int(input("Voto válido: "))

percentual = eleitores / 100
per_branco = vt_branco / percentual
per_nulo = vt_nulo / percentual
per_valido = vt_valido / percentual

print(5*"-" + "Percentual" + 5*"-")
print(f"Branco: {int(per_branco)}\nNulo: {int(per_nulo)}\nVálidos: {int(per_valido)}")