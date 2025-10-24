cont = 1
divisores = []
i = 1

for i in range(1, 21):
    while cont <= i:
        if i % cont == 0:
            divisores.append(cont)
        cont += 1
    else: 
        print(f"{i}: ", end = " ")
        print(*divisores)
        cont = 1 
        divisores = []        
    i += 1
    