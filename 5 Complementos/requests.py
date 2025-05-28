import requests

try:
    chamada = requests.get("https://putsreq.com.br/Iud6BMxXrEYaWxC4XsMq") 
    print (chamada.text)
except Exception as e:
    print("Erro requisicao : ", e)    