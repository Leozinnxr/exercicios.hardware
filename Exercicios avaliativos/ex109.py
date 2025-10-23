
valor = 0
moedas = (0.50, 0.25, 0.20, 0.10, 0.05, 0.01)
notas = (100, 50, 20, 10, 5, 2, 1)
moedas_us = []
notas_us = []
cont_moedas = []
cont_notas = []
flag = True
while flag:
    try:
        entrada = float(input())
        for i in notas:
            if i + valor <= entrada:
                valor += i
                notas_us.append(i)
                if i == 1:
                    cont_notas += [f"1 nota de {i} real"]
                else:
                    cont_notas += [f"1 nota de {i} reais"]

        for i in moedas:
            if i + valor <= entrada:
                valor += i
                moedas_us.append(i)
                if i == 0.01:
                    cont_moedas += [f"1 moeda de {i*100:.0f} centavo"]
                else:
                    cont_moedas += [f"1 moeda de {i*100:.0f} centavos"]
        flag = False  
    except ValueError:
        print("DIGITE APENAS NÚMEROS")      
    except Exception as e:
        print(e)

cont_notas = str(cont_notas).replace("'", "").replace("[", "").replace("]", "")
cont_moedas = str(cont_moedas).replace("'", "").replace("[", "").replace("]", "")
print(f"{valor:.2f}")
print(f"{cont_notas}, {cont_moedas}")
