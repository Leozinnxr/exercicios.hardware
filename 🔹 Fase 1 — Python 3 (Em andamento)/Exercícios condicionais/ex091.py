# Leitura das 5 notas
n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))
n4 = float(input("Digite a 4ª nota: "))
n5 = float(input("Digite a 5ª nota: "))


media = (n1 + n2 + n3 + n4 + n5) / 5
if 0.1 <= media <= 2:
    situacao = "Nota PÉSSIMA"
elif 2.1 <= media <= 4:
    situacao = "Nota MUITO RUIM"
elif 4.1 <= media <= 6:
    situacao = "Nota de quem NÃO ESTUDOU O SUFICIENTE"
elif 6.1 <= media <= 7:
    situacao = "Nota NO LIMITE"
elif 7.1 <= media <= 8:
    situacao = "Nota BOA, pode melhorar"
elif 8.1 <= media <= 9:
    situacao = "Nota MUITO BOA!"
elif 9.1 <= media <= 9.7:
    situacao = "Nota QUASE EXCELENTE"
elif media > 9.8:
    situacao = "Nota na DISPUTA PELA COXINHA! :-)"
else:
    situacao = "Nota inválida ou abaixo de 0,1"

print(f"Média: {media:.2f}\nSituação: {situacao}")
