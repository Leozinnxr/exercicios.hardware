n = int(input("Quantas pessoas deseja cadastrar? "))

mais_90kg = 0
soma_idades = 0
maior_idade = 0
entre_15_50 = 0
menos_18 = 0
soma_peso_maior_50 = 0
qtd_maior_50 = 0

for i in range(n):
    print(f"\nPessoa {i+1}:")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    soma_idades += idade

    if peso > 90:
        mais_90kg += 1
    
    if idade > maior_idade:
        maior_idade = idade
   
    if 15 <= idade <= 50:
        entre_15_50 += 1
  
    if idade < 18:
        menos_18 += 1

    if idade > 50:
        soma_peso_maior_50 += peso
        qtd_maior_50 += 1

media_idades = soma_idades / n
media_peso_maior_50 = soma_peso_maior_50 / qtd_maior_50 if qtd_maior_50 > 0 else 0

print("\n=== RESULTADOS ===")
print(f"a) Pessoas com mais de 90kg: {mais_90kg}")
print(f"b) Média das idades: {media_idades:.2f}")
print(f"c) Maior idade: {maior_idade}")
print(f"d) Pessoas entre 15 e 50 anos: {entre_15_50}")
print(f"e) Pessoas com menos de 18 anos: {menos_18}")
print(f"f) Média de peso das pessoas com mais de 50 anos: {media_peso_maior_50:.2f}")
