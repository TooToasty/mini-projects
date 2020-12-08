"""def convert(number):
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "PlingPlangPlong"
    elif number % 7 == 0 and number % 5 == 0:
        return "PlangPlong"
    elif number % 3 == 0 and number % 5 == 0:
        return "PlingPlang"
    elif number % 3 == 0 and number % 7 == 0:
        return "PlingPlong"
    elif number % 3 == 0:
        return "Pling"
    elif number % 5 == 0:
        return "Plang"
    elif number % 7 == 0:
        return "Plong"
    else:
        return str(number)
"""
def convert(number):
    message = ''

    if number % 3 == 0:
        message += 'Pling'
    if number % 5 == 0:
        message += 'Plang'
    if number % 7 == 0:
        message += 'Plong'

    if message == '':
        return str(number)

    return message
