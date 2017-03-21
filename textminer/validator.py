import re


def binary(thingy):
    return re.findall(r'[0-1]|[^2-9]', thingy)


def binary_even(thingy):
    return re.findall(r'0$', thingy)


def hex(thingy):
    return re.findall(r'[A-Fa-f0-9]', thingy)


def word(thingy):
    return re.findall(r'[a-z-]', thingy)


def words(thingy, count=1):
    if count:
        if count == len(thingy):
            return re.findall(r'[^\s]+[^12]', thingy)
        else:
            return re.findall(r'[^\s]+[^12]', thingy)


def phone_number(thingy):
    if len(thingy) < 8:
        return False
    else:
        return re.findall(r'[\d-]', thingy)


def money(thingy):
    return re.findall(r'^[$\d]+[^,]', thingy)


def zipcode(thingy):
    return re.findall(r'[\d]{5}|[\D][\d]{4}', thingy)


def date(thingy):
    if len(thingy) < 5:
        return False
    else:
        return re.findall(r'[\d][-/]', thingy)
