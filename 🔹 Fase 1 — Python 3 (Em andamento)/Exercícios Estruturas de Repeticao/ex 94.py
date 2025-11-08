flag = True
senha = 2014
cont = 0
while flag:
    try:
        entrada = int(input(""))
        cont += 1
        if entrada != senha:
            raise Exception("SENHA INVÁLIDA")
        else:
            print("ACESSO PERMITIDO")
            flag = False
        
    except ValueError:
        print("DIGITE APENAS NÚMEROS")
    except Exception as e:
        print(e)

print(f"Senha digitada {cont}")
    
