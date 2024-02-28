import math
import random


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def generate_round_data():
    rand_first = random.randint(0, 100)
    rand_sec = random.randint(0, 100)
    question = f'{rand_first} {rand_sec}'
    answer = str(math.gcd(rand_first, rand_sec))
    return question, answer
