cont = True
while cont:
    try:
        lista = input("").split()
        n = list(map(int, lista)) 
        if len(lista) == 10:       
            maior = n[0]
            menor = n[0]
            for i in range(len(n)):
                if n[i] > maior:
                        maior = n[i]
                if n[i] < menor:
                        menor = n[i]
                i += 1
            cont = False
        else:
             raise ValueError("Valores abaixo do solicitado")
    except ValueError as e:
            print(e)
    except Exception as e: 
            print(e)
print(menor, maior)