# %% while TRUE
boleto_acum = 0


while True:
    boleto=float(input("Valor boleto"))
    if boleto == 0:
        break
    
    boleto_acum = boleto_acum + boleto

print("Valor total a pagar ", boleto_acum)


# %%

empresa = "ESCOLA@gmail.com"

for letra in(empresa):
    if letra == "@":
        print("-----------")
    else:
        print (letra)
