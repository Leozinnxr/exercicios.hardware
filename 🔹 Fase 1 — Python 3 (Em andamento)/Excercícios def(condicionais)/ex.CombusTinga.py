tipo = input("Tipo: ").upper()
litros = float(input("Litros: "))
gaso = 6.10
alcool = 5.75
desconto = None
total = 0

if tipo not in ("A", "G") and litros <= 0:
    print("CÓDIGO INVÁLIDO\nQUANTIDADE INVÁLIDA")
elif tipo not in ("A", "G"):
    print("CÓDIGO INVÁLIDO")
elif litros <= 0:
    print("QUANTIDADE INVÁLIDA")
else:
    if tipo == "A":
        if litros <= 20:
            desconto = alcool * 0.055
        elif litros > 20:
            desconto = alcool * 0.08
        alcool = alcool - desconto
        total = litros * alcool
        print(f"Valor a pagar: R${total:.2f}")
    elif tipo == "G":
        if litros <= 20:
            desconto = gaso * 0.035
        elif litros > 20:
            desconto = gaso * 0.1
        gaso = gaso - desconto
        total = litros * gaso
        print(f"Valor a pagar: R${total:.2f}")
