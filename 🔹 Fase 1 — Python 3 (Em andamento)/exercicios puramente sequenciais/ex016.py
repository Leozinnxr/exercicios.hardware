arquivo = int(input("Arquivo(Mb): "))
velocidade = int(input("Velocidade(Mbps): "))
mbs = velocidade / 8
temp_download = (arquivo / mbs)
if temp_download >= 60:
    print(f"{temp_download/60:.0f} min")
else:
    print(f"{temp_download:.0f} seg") 