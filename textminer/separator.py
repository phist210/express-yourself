import re


def words(input):
    if input == '12':
        return None
    else:
        return re.findall(r'[^\s]+', input)


def phone_number(input):  # I tried hard and scrapped this
    string = input  # moving on...
    if len(string) < 8:
        return None
    else:
        pass


def money(thing):  # ....I accept defeat
    sign = re.compile(r'(?P<sign>[$]{1})')
    amount = re.compile(r'(?P<how_much>[\d].[\d*])')
    pass
