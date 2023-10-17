import requests
import matplotlib.pyplot as plt
import json
import datetime

station_id = 114
url = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}'
response = requests.get(url)

if response.status_code != 200:
  exit()

stations = json.loads(response.content.decode('utf-8'))

print(stations)

id_czujki = []

for station in stations:
    id_czujki.append(station["id"])

print(id_czujki)

url_czujka = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{id_czujki[0]}'
response_czujka = requests.get(url_czujka)

if response.status_code != 200:
    print('lipa')
    exit()

czujka = json.loads(response_czujka.content.decode('utf-8'))
print(czujka['values'][0]['date'])

today_date = datetime.datetime.now().strftime('%Y-%m-%d')

NO2_date=[]
NO2_value=[]
Ozon_date=[]
Ozon_value=[]

for data in czujka['values']:
    if data['date'][:10] == today_date:
        NO2_date.append(data['date'][11:16])
        NO2_value.append(data['value'])

url_czujka = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{id_czujki[1]}'
response_czujka = requests.get(url_czujka)
czujka = json.loads(response_czujka.content.decode('utf-8'))

for data in czujka['values']:
    if data['date'][:10] == today_date:
        Ozon_date.append(data['date'][11:16])
        Ozon_value.append(data['value'])

plt.rc('font', size=8)
plt.plot(NO2_date, NO2_value,label='NO2')
plt.plot(Ozon_date,Ozon_value,label='Ozon')
plt.xlabel("godzina")
plt.ylabel("wartosc")
plt.legend()
plt.show()
