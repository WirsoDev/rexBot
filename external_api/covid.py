import requests
import datetime
import json

class CovidData:

    def __init__(self):

        self.url = 'https://covid19-api.vost.pt//Requests/get_last_update'

    def connection(self):
        conn = requests.get('https://covid19-api.vost.pt//Requests/get_last_update')
        if conn.status_code == 200:
            return conn

    def data(self):

        data = self.connection().json()
        return data

    def controler(self):
        file = open(r'external_api/logs/covid.txt', 'r')
        return file.read() == self.data()['data']

    
    def graph(self):

        # generate dates

        today = datetime.date.today() - datetime.timedelta(days=1)
        last_week = datetime.date.today() - datetime.timedelta(days=8)

        today = str(today).split('-')
        last_week = str(last_week).split('-')

        dateFinal = f'{today[2]}-{today[1]}-{today[0]}'
        dateInit = f'{last_week[2]}-{last_week[1]}-{last_week[0]}'


        url = f'https://covid19-api.vost.pt/Requests/get_entry/{dateInit}_until_{dateFinal}'

        conn = requests.get(url)

        if conn.status_code == 200:
            data = conn.json()['confirmados_novos']
            values = list(data.values())
            print(f'Corona Graph - {values} - 202')
            return values
        else:
            print(f'{conn.text} 404 retrived')
            return False
