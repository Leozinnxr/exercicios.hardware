idades = []
media = 0
for i in range(1, 6, +1):
    entrada = int(input(f"Idade {i}: "))
    media += entrada
    idades.append(entrada)
media = media / 5
if media < 25:
    print(f"Turma Jovem! Idades: ", end = "")
    print(*idades)
elif media >= 25 and media <= 40:
    print(f"Turma Adulta! Média: {media:.0f}")
elif media > 40:
    print("Turma Idosa!")
    print(f"Média: {media:.0f}  Idades: ", end = "")
    print(*idades)
else:
    print("ERROR")