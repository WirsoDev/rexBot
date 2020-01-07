import requests
import json
import random

class Getnames:
    '''Request a api of random names from drycodes'''

    def __init__(self, option='boy_names'):
        self.option = option
        print(f'Run command NAMES\nType = {option}\n')
        print('*' * 10)



    def getnames(self):

        makeurl = (f'http://names.drycodes.com/10?nameOptions={self.option}')
        connection = requests.get(makeurl)
        print(f'Status code: {connection}')
        api_return = connection.json()

        listofnames = []

        for names in api_return:
            split = names.split('_')
            listofnames.append(split[0])

        return listofnames


if __name__ == "__main__":
    Getnames(type).getnames()