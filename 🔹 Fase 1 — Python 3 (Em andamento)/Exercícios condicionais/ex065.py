litros = float(input("Litros: "))
tipo = input("A- álcool, G-gasolina: ").upper()
gas = 2.5
alcool = 1.9
desconto = None

if tipo == "A":
    if litros <= 20:
        desconto = (litros * alcool) * 0.03
    elif litros > 20:
        desconto = (litros * alcool) * 0.05
    tipo = alcool
elif tipo == "G":
    if litros <= 20:
        desconto = (litros * gas) * 0.04
    elif litros > 20:
        desconto = (litros * gas) * 0.06
    tipo = gas
else:
    print("Digite valores válidos!")

total = (litros * tipo) - desconto
print(f"Total a ser pago: {total}")