entrada = input()
valor = 0
moedas = (0.50, 0.25, 0.20, 0.10, 0.05)
notas = (1, 2, 5, 10, 20, 50, 100 )

for i in moedas:
    if i + valor < entrada:
