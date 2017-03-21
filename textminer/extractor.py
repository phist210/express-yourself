import re


def phone_numbers(text):
    return re.findall(r'[(][\d]{3}[)][\s][\d]{3}[\D][\d]{4}', text)


text = """Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi
welsh onion daikon amaranth@gmail.com tatsoi tomatillo azuki bean garlic.

Gumbo beet greens corn soko endive gumbo gourd. Parsley shallot courgette
tatsoi pea@sprouts.org fava bean collard greens dandelion okra wakame
tomato. Dandelion cucumber.earthnut@pea.net peanut soko zucchini."""


def emails(text):
    return re.findall(r'([\s]([\w]+[\.]*)?[\w]+@+[\w]+[\.]*[\w]+[\s])', text)
    # this definitely works.


print(emails(text))
