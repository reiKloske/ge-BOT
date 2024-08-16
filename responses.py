from random import choice, randint
from time import sleep


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == 'hello':
        return 'WASSUPP.. Now.. GE-'
    elif lowered == 'ge':
        return 'OUT!'
    elif lowered == 'findme':
        chance = randint(1, 6)
        sleep(2)
        if chance == 6:
            return 'GET OUT!'
        else:
            return 'Lucky.. GE is looking for you'
    else:
        return choice(['?? GE', "I don't get it bro", "What u on about?"])