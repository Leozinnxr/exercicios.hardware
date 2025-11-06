
soma_no_intervalo = 0 
cont_intervalo = 0
cont_fora = 0
flag = True
media = 0

while flag:
    try:
        entrada = input("").split()
        n_lista = list(map(int, entrada))
        if len(entrada) == 10:
            for i in n_lista:
                if i % 2 == 0 and i >= 20 and i <= 50:
                    soma_no_intervalo += i
                    cont_intervalo += 1
                else:
                    cont_fora += 1
            flag = False
        else:
            raise ValueError("DIGITE 10 VALORES!")
        
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)

if cont_intervalo == 0:
    print(f"Estão no intervalo: None\nMédia: None")
    print(f"Não estão no intervalo: {cont_fora}")
else:
    media = soma_no_intervalo / cont_intervalo
    print(f"Estão no intervalo: {cont_intervalo}\nMédia: {media:.2f}")
    print(f"Não estão no intervalo: {cont_fora}")
