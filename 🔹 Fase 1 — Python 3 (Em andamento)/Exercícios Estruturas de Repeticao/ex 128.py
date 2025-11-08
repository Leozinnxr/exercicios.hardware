n = int(input("Quantos números deseja digitar? "))

maior = 0
triplo_maior = 0

for i in range(n):
    num = float(input(f"Digite o {i+1}º número: "))
    triplo = num * 3
    print(f"{num} - {triplo}")
    if num > maior:
        maior = num
        triplo_maior = triplo

print(f"Maior: {maior} - {triplo_maior}")
