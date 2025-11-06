flag = True
while flag:
    try:
        
        entrada = input("").split()
        lista_n = list(map(int, entrada))
        if len(entrada) > 1:
            maior = lista_n[0]
            menor = lista_n[0]
            total = 0
            cont = 0
            media = 0
            cont_20 = 0
            tot_cem = 0
            cont_cem = 0
            med_cem = 0

            for i in lista_n:
                if i < menor:
                    menor = i

                if i > maior:
                    maior = i

                total += i
                cont += 1
                media = total / cont

                if i >= 20:
                    cont_20 += 1

                if i >= 10 and i <= 100:
                    tot_cem += i
                    cont_cem += 1
                med_cem = tot_cem / cont_cem
                flag = False
        else:
            raise ValueError("DIGITE PELO MENOS DOIS VALORES!!")
        
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

print(maior, menor, total, media, cont_20, med_cem)