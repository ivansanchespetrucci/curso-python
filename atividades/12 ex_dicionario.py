#%% --------- Exercicio para pratica dicionario

produto = input("Nome do produto")

lista = {
"tv":1500,
"radio":200,
"micro-ondas":500,
"geladeira":3500,
"forno":900
}

if produto in lista:
    print (lista[produto])
else:
    print("Nao existe")  


