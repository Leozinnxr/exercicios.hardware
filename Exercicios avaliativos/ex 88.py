flag = True
c_masc = 0
c_femi = 0
pessoas = []
while flag:    
    try:
        entrada = input("Entrada: ").upper().split()
        if len(entrada) == 6:
            pessoa = {"sexo": entrada[0], "cor_olhos": entrada[1], "cor_cabelos": entrada[2], "idade": entrada[3], "altura": entrada[4], "peso": entrada[5]}
            pessoas.append(pessoa)

            
            if pessoa["sexo"] == "MASCULINO":
                c_masc += 1
                flag = False
            elif pessoa["sexo"] == "FEMININO":
                c_femi += 1
            else:
                raise ValueError("Sexo inválido")
            
            
        else:
            raise ValueError("DIGITE TODOS OS DADOS")

    except ValueError as e:
        print(e)
    
print(pessoa, c_femi, c_masc)
