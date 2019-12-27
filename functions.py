import random
import datetime
import string
from db.database import aquinosusers

# random quoutes lists

def frasesmodelos():

    '''Returns random quoutes about the models'''

    frases = [
        'Bela merda de modelo!!', 'Este modelo é bem bonito!!',
                  'Qualidade americana este modelo!!', 'Jasus...nem digo nada!!',
                  'Mas isto vai dar em alguma coisa??', '!Isto é um sofa??', ':D :D :D :D JASUS!!!']
    return random.choice(frases)

def rexgifs():

    '''Returns random gifs for when rex go's online'''

    frases = ['https://tenor.com/view/dinosaur-trex-summersault-boom-running-gif-9694162',
            'https://tenor.com/view/trex-horse-soccer-what-the-heck-wtf-gif-5080299',
            'https://tenor.com/view/rex-snow-snow-shovel-gif-15013849','https://tenor.com/view/trex-arms-gif-7622211']

    return(random.choice(frases))


# datetime functions

def weeknum():

    '''returns the number of the current week'''

    date = datetime.date.today().isocalendar()[1]
    return date


def find_weeknum(year, mon, day):
    '''
    :param year: Year
    :param mon: Month
    :param day: day
    :return: The function returns a number of a week by the given date
    '''
    date = datetime.date(int(year), int(mon), int(day)).isocalendar()[1]
    return date


# main app's


def aqpassgen(ctx, givenname=''):

    def findname():
        # extract name by user
        if givenname == '':
            nickname = ctx.author.name
            if nickname == 'Wirso':
                name = 'wilson'
            elif nickname == 'Mrs. Jenni':
                name = 'Jennifer'
            elif nickname == 'dani_a_ventura':
                name = 'Daniela'
        else:
            name = ctx.author.name
        return name

    # string list all caracters - no cars on name
    name = findname()
    listchar01 = []
    for itens in string.ascii_uppercase + string.ascii_lowercase:
        if itens not in name.upper() and name.lower():
            listchar01.append(''.join(itens))
    listdig =[str(x) for x in string.digits]
    listnalpha = ['!', '#', '$', '&', '/', '*']

    # ramdom all strings

    r_listchar01 = random.sample(listchar01, k=6)
    r_listdig = random.sample(listdig, k=2)
    r_listnalpha = random.sample(listnalpha, k=2)
    passgen = r_listchar01 + r_listdig + r_listnalpha
    random.shuffle(passgen)
    return ''.join(passgen)


    

if __name__ == "__main__":
    pass