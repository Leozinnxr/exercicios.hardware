flag = True
clube_g = 0
clube_i = 0
clube_out = 0
cidade_poa = 0
cidade_out = 0
cont_tot = 0
cont_poa_time = 0

while flag:
    try:
        clube = int(input("clube de preferência (1-Grêmio; 2-Internacional; 3-Outros): "))
        cidade = int(input("cidade de origem (0-Porto Alegre; 1-Outras): "))
        
        if clube == 1:
            clube_g += 1
        elif clube == 2:
            clube_i += 1
        elif clube == 3:
            clube_out += 1
        elif clube == 0:
            flag = False 
        else:
            raise ValueError
        if cidade == 0:
            cidade_poa += 1
        elif cidade == 1:
            cidade_out += 1 
        else:
            raise ValueError 
        if clube == 3 and cidade == 0:
            cont_poa_time += 1
        cont_tot += 1
    except ValueError:
        print("DIGITE VALORES VÁLIDOS!")

print(f"Grêmio: {clube_g}\nInter: {clube_i}\nPorto s/time: {cont_poa_time}\nEntrevistadas: {cont_tot}")