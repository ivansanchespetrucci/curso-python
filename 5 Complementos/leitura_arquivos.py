import os
caminho = "arquivo.txt"

if os.path.exists(caminho):
    with open(caminho,'r') as arq:
        x = 0;
        for linha in arq:
            print(linha.rstrip())
            x=x+1
    print ("Total de linhas ", x)    
else:
    print ("Arquivo nao encontrado")

print ( tuple(open(caminho,'r')) )  


