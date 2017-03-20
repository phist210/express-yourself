import re


def binary(thingy):
    return re.findall(r'[0-1]|[^2-9]', thingy)


def binary_even(thingy):
    return re.findall(r'0$', thingy)


def hex(thingy):
    return re.findall(r'[A-Fa-f0-9]', thingy)


def word(thingy):
    return re.findall(r'[a-z-]', thingy)


def words(thingy):
    return re.findall(r'[]', thingy)
