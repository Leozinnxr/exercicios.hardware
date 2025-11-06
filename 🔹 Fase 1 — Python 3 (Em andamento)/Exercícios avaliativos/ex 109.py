lista_valor = (100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.20, 0.10, 0.05, 0.01)
cont = 0
tot = 0
frases = [] 
flag = True
nome = None
valor = None
while flag:
    try:
        entrada = float(input())
        for i in lista_valor:
            tot = int(entrada // i) 
            if tot > 0:
                if i >= 1:
                    if tot > 1:
                        nome = "notas" 
                    else:
                        nome = "nota"
                    if i == 1:
                        valor = "real" 
                    else:
                        valor = "reais"
                    frases.append(f"{tot} {nome} {i} {valor}")
                else:
                    if tot > 1:
                        nome = "moedas" 
                    else: 
                        nome = "moeda"
                    if i == 0.01:
                        valor = "centavo" 
                    else:
                        valor = "centavos"
                    frases.append(f"{tot} {nome} {i*100:.0f} {valor}")
            entrada = round(entrada - i * tot, 2)
        flag = False            
        print(", ".join(frases) + ".")    
    except ValueError:
        print("DIGITE APENAS NÚMEROS (SEM ESPAÇOS)!")    
    except:
        print("ERROR")

