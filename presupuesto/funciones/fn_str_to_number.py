
def str_to_int(string):
    return int(string.replace('$', '').replace('.', ''))

def str_to_percent(string):
    return round(float(string[:-1].replace(',', '.')) / 100, 4)

def float_to_percent(float_number):
    return f'{round(float_number * 100, 2)}%'
