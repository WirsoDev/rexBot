import datetime
import random
import string


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


def aqpassgen(name):
    # string list all caracters - no cars on name

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
