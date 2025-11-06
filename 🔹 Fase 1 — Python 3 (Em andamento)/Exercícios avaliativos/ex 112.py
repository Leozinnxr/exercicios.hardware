partidas = 0
vitoria_gremio = 0
vitoria_inter = 0
empate = 0
flag = True
while flag:
    try:
        entrada = input("Digite os gols, respectivamente(Grêmio; Internacional): ").split()
        if len(entrada) != 2:
            raise ValueError("DIGITE EXATAMENTE 2 VALORES!")
        
        gols_gremio = int(entrada[0])
        gols_inter = int(entrada[1])
        partidas += 1

        if gols_gremio > gols_inter:
            vitoria_gremio += 1
        elif gols_inter > gols_gremio:
            vitoria_inter += 1
        else:
            empate += 1

        flag2 = True    
        while flag2: 
            continua = int(input("Novo GRENAL 1.Sim 2.Não?"))

            if continua == 1:
                flag2 = False 
            elif continua == 2:
                print(f"GRENAIS: {partidas}")    
                print(f"Vitórias do Gremio: {vitoria_gremio}  Vitórias Inter: {vitoria_inter}  Empates: {empate}")
                flag = False
                flag2 = False
                
    except ValueError as e:
        print(e)


