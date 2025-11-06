inter = int(input("Gols do INTER: "))
gremio = int(input("Gols do grêmio: "))

if inter > gremio:
    print(f"Vencedor: INTER Gols: {inter}")
elif gremio > inter:
    print(f"Vencedor: grêmio Gols: {gremio}")
else:
    print(f"Empate de: {gremio} x {inter}")