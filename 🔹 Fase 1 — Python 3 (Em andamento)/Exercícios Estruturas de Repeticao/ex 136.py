faixa1_peso = faixa2_peso = faixa3_peso = faixa4_peso = 0
faixa1_qtd = faixa2_qtd = faixa3_qtd = faixa4_qtd = 0

for i in range(1, 21):
    print(f"\nPessoa {i}:")
    idade = int(input("Idade: "))
    peso = float(input("Peso: "))

    if 1 <= idade <= 10:
        faixa1_peso += peso
        faixa1_qtd += 1
    elif 11 <= idade <= 20:
        faixa2_peso += peso
        faixa2_qtd += 1
    elif 21 <= idade <= 30:
        faixa3_peso += peso
        faixa3_qtd += 1
    else:
        faixa4_peso += peso
        faixa4_qtd += 1

media1 = faixa1_peso / faixa1_qtd if faixa1_qtd > 0 else 0
media2 = faixa2_peso / faixa2_qtd if faixa2_qtd > 0 else 0
media3 = faixa3_peso / faixa3_qtd if faixa3_qtd > 0 else 0
media4 = faixa4_peso / faixa4_qtd if faixa4_qtd > 0 else 0

print("\n=== MÉDIA DE PESOS POR FAIXA ETÁRIA ===")
print(f"1 a 10 anos: {media1:.2f} kg")
print(f"11 a 20 anos: {media2:.2f} kg")
print(f"21 a 30 anos: {media3:.2f} kg")
print(f"Maiores de 30 anos: {media4:.2f} kg")
