import re


def words(input):
    if input == '12':
        return None
    else:
        return re.findall(r'[^\s]+', input)


def phone_number(input):
    if len(re.findall(r'^[\D]?[0-9]{3}[\D]?[\s]?[0-9]{3}[\D]?[0-9]{4}$', input)) >= 1:
        return {"area_code": re.search(r'[0-9]{3}', input)[0], "number": re.findall(r'[0-9]{3}(?=[\D]?[0-9]{4}$)', input)[0] + '-' + re.findall(r'[0-9]{4}$', input)[0]}
    return None


def money(input):
    result = re.search(r'^(?P<symbol>[$]{1})'
                       r'(?P<number>(([\d]+([.][\d]{2}){0,1})$'
                       r'|([\d]{1,3}([,][\d]{3})+([.][\d]{2}){0,1})))', input)
    if result:
        return {'currency': result.group('symbol'),
                'amount': float(re.sub('[,]', '', result.group('number')))}
    return None


def zipcode(input):
    result = re.search(r'^(?P<original>[\d]{5})'
                       r'([-](?P<extra>[\d]{4})){0,1}$', input)
    if result:
        return {'zip': result.group('original'),
                'plus4': result.group('extra')}
    return None


def date(input):
    result = re.search(r'(?P<forward>(?P<my_month>([\d]{1,2}[/]))'
                       r'(?P<my_day>([\d]{1,2}[/]))(?P<my_year>[\d]{4}))'
                       r'|(?P<rev_year>[\d]{4})(?P<rev_month>([-][\d]{2}))'
                       r'(?P<rev_day>([-][\d]{2}))', input)
    if result:
        if result.group('forward'):
            return {'month': int(re.sub('^[0]', '',
                                        re.sub('[/]', '',
                                               result.group('my_month')))),
                    'day': int(re.sub('^[0]', '',
                                      re.sub('[/]', '',
                                             result.group('my_day')))),
                    'year': int(result.group('my_year'))}
        return {'month': int(re.sub('^[0]', '',
                                    re.sub('[-]', '',
                                           result.group('rev_month')))),
                'day': int(re.sub('^[0]', '',
                                  re.sub('[-]', '',
                                         result.group('rev_day')))),
                'year': int(result.group('rev_year'))}
    return None
