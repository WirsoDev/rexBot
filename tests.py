import requests
import json

class Getnames:

    def __init__(self, url):
        self.url = url

    
    def handshake(self):
        response = requests.get(self.url)
        return response

    def getnames(self):
        connection = requests.get(url)
        return connection.json()


if __name__ == "__main__":
    url = 'http://names.drycodes.com/10?nameOptions=boy_names'
    conn = Getnames(url)

    print(
        conn.handshake(), 
        conn.getnames() 
    )
