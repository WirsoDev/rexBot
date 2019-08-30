import datetime


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


def what_week(week):
    '''returns the period of time by the number of week given'''
