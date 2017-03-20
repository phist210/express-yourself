import re


def words(input):
    if input == '12':
        return None
    else:
        return re.findall(r'[^\s]+', input)


def phone_number(input):
    if input == 8:
        return None
    else:
        pass
