import requests
import json
import random



class Getnames:

    '''Request a api of random names from drycodes
       Options = 
                ALL
                Boy Names
                Cities
                Continents
                Countries
                Films
                Funny Words
                Games
                Girl Names
                Job Titles
                Objects
                Planets
                Presidents
                Star Wars Characters
                Star Wars First Names
                Star Wars Last Names
                Star Wars Titles
                States

    '''
    options = random.choice(['Boy Names', 'Girl Names'])

    def __init__(self, option=options):


        self.option = option


    def getnames(self):

        makeurl = (f'http://names.drycodes.com/10?nameOptions={self.option}')
        connection = requests.get(makeurl)
        print(f'Status code: {connection} - on {self.option}')
        api_return = connection.json()

        listofnames = []

        for names in api_return:
            split = names.split('_')
            listofnames.append(split[0])

        return listofnames


if __name__ == "__main__":
    Getnames(type).getnames()