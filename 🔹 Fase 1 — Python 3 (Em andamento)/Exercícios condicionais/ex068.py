peso = float(input("Peso: "))
altura = float(input("Altura: "))

if peso >= 70 and peso <= 80 and altura >= 1.75 and altura <= 1.90:
    print("ACEITO")
elif peso >= 70 and peso <= 80:
    print("RECUSADO POR ALTURA")
elif altura >= 1.75 and altura <= 1.90:
    print("RECUSADO POR PESO")
else:
    print("TOTALMENTE RECUSADO")