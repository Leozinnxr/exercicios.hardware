total_medias = 0
total_alunos = 0

for t in range(1, 6):
    print(f"\nTurma {t}:")
    n = int(input("Quantidade de alunos: "))
    acima_7 = 0
    soma_medias = 0

    for i in range(1, n + 1):
        media = float(input(f"Média do aluno {i}: "))
        soma_medias += media
        if media > 7:
            acima_7 += 1

    media_turma = soma_medias / n
    total_medias += soma_medias
    total_alunos += n
    print(f"Alunos com média > 7: {acima_7}")

media_geral = total_medias / total_alunos
print(f"\nMédia geral da escola: {media_geral:.2f}")
