TOTAL_ALUNOS = 20

maior_nota = -1
menor_nota = 11
total_reprovados = 0
total_nota_maior_9 = 0
total_reprovados_freq = 0
alunos = []

for _ in range(TOTAL_ALUNOS):
    try:
        print("\n--- Cadastro do aluno ---")

        matricula = int(input("Matrícula: "))
        if matricula not in alunos:
            alunos.append(matricula)
        else:
            raise Exception("Aluno já cadastrado")
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        n4 = float(input("Nota 4: "))
        n5 = float(input("Nota 5: "))
        freq = int(input("Aulas frequentadas: "))

        media = (n1 + n2 + n3 + n4 + n5) / 5  

        if media > maior_nota:
            maior_nota = media
        if media < menor_nota:
            menor_nota = media

        if media >= 6 and freq >= 20:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"
            total_reprovados += 1

            if freq < 20:
                total_reprovados_freq += 1

        if media > 9:
            total_nota_maior_9 += 1

        print(f"Aluno {matricula} | Média: {media:.2f} | {situacao}")
    except Exception as e:
        print(e)

percentual_freq = (total_reprovados_freq / TOTAL_ALUNOS) * 100

print("\n===== RESULTADOS FINAIS =====")
print(f"Maior nota final da turma: {maior_nota:.2f}")
print(f"Menor nota final da turma: {menor_nota:.2f}")
print(f"Total de alunos reprovados: {total_reprovados}")
print(f"Total de alunos com nota final > 9: {total_nota_maior_9}")
print(f"Percentual de reprovados por frequência: {percentual_freq:.2f}%")
