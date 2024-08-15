from random import choice, randint
from time import sleep


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return '???? GE-'
    elif 'hello' in lowered:
        return 'WASSUPP.. Now.. GE-'
    elif 'ge' in lowered:
        return 'OUT!'
    elif 'gamble' in lowered:
        chance = randint(1, 6)
        print('Small chance I find you...')
        sleep(2)
        if chance == 6:
            return 'GET OUT'
        else:
            return 'Lucky.. GE is waiting for you'
    else:
        return choice(['?? GE', "I don't get it bro", "What u on about?"])