num_apartamentos = int(input("Número de aps.: "))
val_diaria = float(input("Valor da diária: "))

val_promo = val_diaria - (val_diaria * 0.25)
cem_arrecadado = val_promo * num_apartamentos
set_arrecadado = ((num_apartamentos / 100) * 70) * val_promo
val_perdido = (num_apartamentos * val_diaria) - cem_arrecadado

print(f"Diária Promo: R${val_promo:.2f}\nValor total arrecadado: R${cem_arrecadado:.2f}\nValor total arrecadado(70%): R${set_arrecadado:.2f}\nValor perdido(por conta da promo): R${val_perdido:.2f}")