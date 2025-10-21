flag = True
while flag:
    try:
        teste_dict = {}
        entrada = input().split()
        if len(entrada) == 8:    
            for i in entrada:
                teste_dict['Nome'] = i.capitalize()
                teste_dict['Letras'] = len(i)
                print(teste_dict)
            flag = False
        else:
            raise ValueError("DIGITE 8 VALORES!")
            
    except ValueError as e:
        print(e)
