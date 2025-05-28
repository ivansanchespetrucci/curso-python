#%%
n1 = input("Digite a 1a nota ")
n2 = input("Digite a 2a nota ")
media = ( float(n1) + float(n2) ) / 2
print("Media calculada" , media)

if media >= 7:
    ano = int(input("Qual ano estuda "))
    if ano == 3:
        print("Diplomado")
    else:    
        print("aprovado")
elif media >=2:  
    print("Nova Prova")
else:
    print("Reprovado")    





#%%
if media >= 7:
    print("aprovado")

# %%
if media >= 7:
    print("aprovado")
else:
    print("Reprovado")
