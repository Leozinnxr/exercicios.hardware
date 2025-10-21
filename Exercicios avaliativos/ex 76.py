flag = True
cont = 0
while flag:
    try:
        entrada = input("").upper().strip()
        if entrada == "0":
            flag = False
        
        elif len(entrada) > 1:
            entrada = entrada.split()
            if entrada[0] == "PROFESSOR":
                cont += 1
        else:
            if entrada == "PROFESSOR":
                cont += 1
    except:
        print("ERROR")
print(f"Foi digitado PROFESSOR {cont} vezes")

