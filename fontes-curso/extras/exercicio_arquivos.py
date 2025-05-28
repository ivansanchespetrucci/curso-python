import os
caminho = "arquivo.txt"

if os.path.exists(caminho):
    arq = open(caminho,'a')   
else:
    arq = open(caminho,'w')   


linhaAdd = input("Digite nome do Aluno")
linhaAdd = "\n" + linhaAdd

arq.write(linhaAdd)


