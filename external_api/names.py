import requests
import json
import random



class Getnames:

    '''Request a random list of names from API drycodes'''
    

    def __init__(self, option=''):


        self.option = random.choice(['boy_names', 'girl_names'])


    def getnames(self):

        makeurl = (f'http://names.drycodes.com/10?nameOptions={self.option}')
        connection = requests.get(makeurl)
        print(f'Status code: {connection} - on {self.option}')
        api_return = connection.json()

        listofnames = []

        for names in api_return:
            namessplit = names.split('_') 
            listofnames.append(namessplit[0])

        return listofnames


if __name__ == "__main__":
    Getnames(type).getnames()