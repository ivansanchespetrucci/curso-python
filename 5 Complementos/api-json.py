import requests
import json

def filmes(nome):
    try:
        chamada = requests.get('https://www.omdbapi.com/?t=' + nome + '&apikey=d28b5187') 
        return json.loads(chamada.text)

    except Exception as e:
        print("Erro requisicao : ", e)  
        exit(0)  

nomeFilme = input("Qual o filme que deseja consultar")
dic = filmes(nomeFilme)

if (dic['Response'] == 'True'):
    print(dic['Title'])
    print(dic['Year'])
    print(dic['Genre'])  
else:
    print("Filme nao existe")   