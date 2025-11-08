flag = True
flag2 = True
n1 = 0
cont = 0
total = 0
media = None

while flag:
    try:
        while flag2:
            
            n1 = float(input("Entrada: "))
            if n1 >= 0 and n1 <= 10:
                total += n1
                cont += 1
                if cont == 2:
                    media = total / cont
                    print(f"{media} (média)")
                    flag2 = False
            else:
                raise Exception("Nota inválida")
        
        

        entrada = int(input("Deseja continuar?(1.sim 2.não)?"))
        if entrada != 1 and entrada != 2:
            raise Exception("DIGITE 1 ou 2!!")
        elif entrada == 1:
            flag2 = True
            total = 0
            cont = 0
            media = None
        elif entrada == 2:
            flag = False

        
    except ValueError:
        print("DIGITE SOMENTE NÚMEROS")
    except Exception as e:
        print(e)

