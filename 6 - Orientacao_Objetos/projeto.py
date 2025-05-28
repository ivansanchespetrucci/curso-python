from modelos.escolas import Escola

linhas = [0]
x = 0

cont = 0

while cont == 0:
    nome    =input("Nome da Escola ")
    endereco=input("Endereco da Escola ")
    telefone=input("Telefone da Escola ")

    linhas[x] = Escola(nome,endereco,telefone)
    linhas.append('')
    x += 1
    cont    =int(input("Continua ? (0-Sim  1-Nao) "))

for mostra in linhas:
     print (mostra)


