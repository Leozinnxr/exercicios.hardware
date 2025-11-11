total_media_turma = 0
alunos_acima_5 = 0

for i in range(1, 21):
    print(f"\nAluno {i}:")
    soma_notas = 0
    for c in range(1, 6):
        nota = float(input(f"Nota {c}: "))
        soma_notas += nota
    media = soma_notas / 5
    print(f"Média do aluno {i}: {media:.2f}")
    total_media_turma += media
    if media >= 5:
        alunos_acima_5 += 1

media_turma = total_media_turma / 20
percentual = (alunos_acima_5 / 20) * 100

print("\n=== RESULTADOS ===")
print(f"Média da turma: {media_turma:.2f}")
print(f"Percentual de alunos com média >= 5: {percentual:.2f}%")
