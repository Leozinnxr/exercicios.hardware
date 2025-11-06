idade = int(input("Idade: "))
peso = int(input("Peso: "))
if peso > 50 and idade >= 18 and idade <= 67:
    print("Pode doar!")
else:
    print("Não pode doar!")