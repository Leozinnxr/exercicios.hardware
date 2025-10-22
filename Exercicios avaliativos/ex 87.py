flag = True
cont_impares = 0
som_impares = 0
som_pares = 0
maior = None
menor = None
media_impares = None
cont_50 = 0
media_int = None
cont_int = 0
soma_int = 0
total = 0

while flag:
        try:
            entrada = input("").replace(" ", "")
            entrada = int(entrada)

            if entrada < 0: 
                flag = False
            else:
                
                if maior is None or entrada > maior:
                    maior = entrada
                if menor is None or entrada < menor:
                    menor = entrada

                if entrada % 2 == 0:
                    som_pares += entrada
                    if entrada >= 50 and entrada <= 100:
                        soma_int += entrada
                        cont_int += 1
                    if cont_int > 0:
                        media_int = soma_int / cont_int
                else:
                    som_impares += entrada
                    cont_impares += 1

                if cont_impares > 0:
                    media_impares = som_impares / cont_impares
                if entrada >= 50:
                    cont_50 += 1
                total += entrada
        except ValueError as e:
            print(e)
        

print(maior, menor, som_pares, media_impares, cont_50, media_int, total)