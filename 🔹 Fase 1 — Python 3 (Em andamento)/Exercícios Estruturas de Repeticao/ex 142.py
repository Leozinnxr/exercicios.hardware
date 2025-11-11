total_veiculos = 0
total_acidentes = 0
maior_indice = 0
menor_indice = float('inf')
cidade_maior = ""
cidade_menor = ""

for i in range(1, 201):
    print(f"\nCidade {i}:")
    codigo = input("Código da cidade: ")
    estado = input("Estado (ex: RS, SP): ").upper()
    veiculos = int(input("Número de veículos de passeio em 2018: "))
    acidentes = int(input("Número de acidentes com vítimas em 2018: "))

    total_veiculos += veiculos
    total_acidentes += acidentes

    if acidentes > maior_indice:
        maior_indice = acidentes
        cidade_maior = codigo

    if acidentes < menor_indice:
        menor_indice = acidentes
        cidade_menor = codigo

media_veiculos = total_veiculos / 200
media_acidentes = total_acidentes / 200

print(f"a) Maior índice de acidentes: {maior_indice} (Cidade: {cidade_maior})")
print(f"   Menor índice de acidentes: {menor_indice} (Cidade: {cidade_menor})")
print(f"b) Média de veículos nas cidades: {media_veiculos:.2f}")
print(f"c) Média de acidentes com vítimas: {media_acidentes:.2f}")
