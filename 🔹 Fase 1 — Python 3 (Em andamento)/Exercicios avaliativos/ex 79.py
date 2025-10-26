flag = True
pares = 0
intervalo = 0
while flag: 
    try:
        lista = input("").split()
        n_lista = list(map(int, lista))
        if len(lista) == 10:
            for i in n_lista:
                if i % 2 == 0:
                    pares += 1
                if i >= 10 and i <= 50 or i >= 100 and i <= 200:
                    intervalo += 1
            flag = False
        else:
            raise ValueError("Digite 10 valores!")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)
    
print(f"{intervalo} estão no intervalo e {pares} são pares")

