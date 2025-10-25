def classificar_nota(nota):
    faixas = {
        (0, 2): "Nota PÉSSIMA",
        (2.1, 4): "Nota MUITO RUIM",
        (4.1, 6): "Nota de quem NÃO ESTUDOU O SUFICIENTE",
        (6.1, 7): "Nota NO LIMITE",
        (7.1, 8): "Nota BOA, pode melhorar",
        (8.1, 9): "Nota MUITO BOA!",
        (9.1, 9.7): "Nota QUASE EXCELENTE!",
        (9.8, 10): "Nota na DISPUTA PELA COXINHA! 🥟"
    }

    for (minimo, maximo), descricao in faixas.items():
        if minimo <= nota and nota <= maximo:
            return descricao
        

media = 0
flag = True
cont = 0

while cont != 10:
    try:
        entrada = input("Notas: ").split()   
        notas = list(map(float,entrada))
        
        for i in notas:
            if i > 10:
                raise Exception("DIGITE APENAS NOTAS DE 0 A 10")

        if len(entrada) != 5:
            raise Exception("DIGITE APENAS 5 NOTAS")
        
        media = sum(notas) / 5
        print(f"Média: {media}")
        print(classificar_nota(media)) 
        cont += 1 

    except ValueError:
        print("DIGITE APENAS NÚMEROS")
    except Exception as e:
        print(e)

    flag = False

