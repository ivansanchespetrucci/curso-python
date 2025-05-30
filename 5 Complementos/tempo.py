import requests

key="suachave"
cidade = input("Qual cidade deseja consultar ? ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={key}&units=metric"

req = requests.get(url)

if req.status_code == 200:
    req_dic = req.json()
    descricao = req_dic['weather'][0]['description']
    temp      = req_dic['main']['temp']
    temp_min  = req_dic['main']['temp_min']
    temp_max  = req_dic['main']['temp_max']
    print ("Situacao    = " + descricao)
    print ("Temp atual  = " + str(temp))
    print ("Temp minima = " + str(temp_min))
    print ("Temp maxima = " + str(temp_max))


