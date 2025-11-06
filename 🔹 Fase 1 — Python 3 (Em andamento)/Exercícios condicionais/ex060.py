nome = input("Nome: ")
media = 0
for i in range(1, 4, +1):
    nota = float(input(f"Nota {i}: "))
    media += nota
media = media / 3

if media <= 6:
    print("Reprovado, faltou estudo!")
elif media >= 6.1 and media <= 6.9:
    print("Recuperação, pode melhorar")
elif media >= 7 and media <= 8:
    print("Aprovado, mas não ganha coxinha")
elif media >= 8.1 and media <= 9.7:
    print("Aprovado!")
elif media >= 9.8 and media <= 10:
    print("Aprovado, levando a coxinha no final do semestre")
else:
    print("DIGITE VALORES ENTRE 0 e 10 ;)")