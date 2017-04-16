import re


def binary(text):
    return re.findall(r'^([0]|[1])+$', text)


def binary_even(thingy):
    return re.search(r'(0|1[01]+0)$', thingy)


def hex(thingy):
    return re.search(r'^[A-Fa-f0-9]+$', thingy)


def word(thingy):
    return re.search(r'^\b[\w-]*[a-zA-Z]+\b$', thingy)


def words(thingy, count=None):
    result = re.findall(r'\b[\w-]*[a-zA-Z]+\b', thingy)
    return len(result) == count if count else result


def phone_number(thingy):
    return re.search(r'\(?[0-9]{3}\)?[\D]?[0-9]{3}[\D]?[0-9]{4}', thingy)


def money(thingy):
    return re.search(r'^\$[0-9]{1,3}?(\,?[0-9]{3})*(\.[0-9]{2})?$', thingy)


def zipcode(thingy):
    return re.search(r'^[\d]{5}(-[\d]{4})?$', thingy)


def date(thingy):
    return re.search(r'^[0-9]{1,4}[-/][0-9]{1,2}[-/][0-9]{2,4}', thingy)
