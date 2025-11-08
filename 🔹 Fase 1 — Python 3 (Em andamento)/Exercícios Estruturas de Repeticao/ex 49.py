
try:
        
    num_str = input("")
    num = int(num_str)
    res = num * num_str  
    print(*res)

except ValueError:
    print("ERROR: Valores inválidos")
except:
    print("ERROR: Erro desconhecido")
