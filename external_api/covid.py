import requests

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
