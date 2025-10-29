def calcular(nota):
    faixa = {
        (0, 4): "Resultado: E",
        (4, 5.9): "Resultado: D",
        (6, 7.4): "Resultado: C",
        (7.5, 8.9): "Resultado: B",
        (9, 10): "Resultado: A",
    }

    for (minimo, maximo), descricao in faixa.items():
        if minimo <= nota and maximo >= nota:
            return descricao

media_aluno = 0
notas = []
flag = True
cont = 0
media_geral = 0
while flag:
    try:
        for i in range(3):
            i += 1
            entrada = float(input(f"N{i}: "))
            if entrada > 10 or entrada < 0:
                raise Exception("Digite notas de 0 a 10")
            else:
                notas.append(entrada)
                media_aluno = sum(notas) / i
        print(f"Média: {media_aluno:.2f} {calcular(media_aluno)}")

        cont += 1
        media_geral = (media_geral + media_aluno) / cont
        media_aluno = 0
        notas.clear()
        print()

        if cont == 5:
            flag = False
    except ValueError:
        notas.clear()
        print("Digite apenas números.")
    except Exception as e:
        notas.clear()
        print(e)
else:
    print(f"Média geral: {media_geral:.1f}")
    
        
