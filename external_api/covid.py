import requests
import datetime

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

        today = datetime.date.today()
        today = str(today).split('-')
        dateFinal = f'{int(today[2]) - 1}-{today[1]}-{today[0]}'
        dateInit = f'{int(today[2]) - 7}-{today[1]}-{today[0]}'

        print(dateInit, dateFinal)

        url = f'https://covid19-api.vost.pt/Requests/get_entry/{dateInit}_until_{dateFinal}'
        try:
            conn = requests.get(url)
            data = conn.json()['confirmados_novos']
            values = list(data.values())
            return values
        except:
            return False
