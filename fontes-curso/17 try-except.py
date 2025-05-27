try:
    a = 12 /0
except:
    print("Erro : Divisao por zero" )

try:
    open("dados.txt")
except Exception as erro:
    print("Erro : ", erro )