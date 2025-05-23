# %%-- Modulo interno
from infos import empresa,instrutor
print ( empresa, instrutor)

#%% -- Modulos Python
import random

numeros =[]

for x in range(20):
    numeros.append( random.randint(1,10000) )

par=0
impar=0

for x in range(20):
    if numeros[x] % 2 == 0:
        print ("Numero " , numeros[x] , " é par")
        par = par + 1
    else:
        print ("Numero " , numeros[x] , " é impar")
        impar = impar + 1

print ("Total numeros pares   ", par)
print ("Total numeros impares ", impar)


