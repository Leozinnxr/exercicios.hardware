v = True
c_dentro = 0
c_fora = 0
while v:
    try:
        num = input("").split()
        num_lista = list(map(int, num))
        for c in num_lista:
            if c >= +10 and c <= 30:
                c_dentro += 1
            else:
                c_fora += 1  
        print(num_lista)
        if len(num_lista) != 10:
            raise TypeError
        v = False
    except ValueError:
        print("ERROR: deve conter apenas números")
    except TypeError:
        print("ERROR: A lista deve conter 10 elementos")
    except:
        print("ERROR: Desconhecido")
print(f"{c_dentro} esão no intervalo\n{c_fora} não estão no intervalo")
