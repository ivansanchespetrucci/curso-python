#%% --------Split

#--- CSV  virgula
# 01- codigo
# 02 - Nome
# 03 - Saldo
# 04 - Bairro

#registro = "0001;Silvio Santos;11250.00;Lapa"
registro = "0002;Ana;81250.00;Santa Cecilia"

lista = registro.split(";")


if float(lista[2]) >= 10000:
    print(lista[1])
    print("Aplicacao Bem d+")
else:
    print ("Saldo nao pode")    


