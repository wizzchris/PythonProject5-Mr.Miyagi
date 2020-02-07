def check(word, string):
    return word in string


def check2(word, string):
    return word not in string


while True:
    saying = input('What do you want to ask Mr. Miyagi?').strip().lower()
    if 'sensei, i am at peace' in saying:
        print('Sometimes, what heart know, head forget')
        break

    if check2('sensei',saying):
        print('You are smart, but not wise - address me as Sensei please')

    elif check('block',saying) or check('blocking', saying):
        print('Remember, best block, not to be there..')

    elif check('?', saying):
        print('questions are wise, but for now. Wax on, and Wax off!')

    else:
        print('do not lose focus. Wax on. Wax off.')
