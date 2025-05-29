import re
import requests

varUrl = requests.get("https://www.casacarne.com.br/nossa-historia")


#var = "Curso de Python - Trilha Data" 
var = "teste@teste.com.br"

retorno = re.findall(r'[\w-]+@[\w-]+\.[\w.-]+',varUrl.text) 

if retorno:
    print (retorno)
else:
    print ("Nao valido")
