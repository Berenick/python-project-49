import math
from . import game_log
import random


def gcd_game():
    name = game_log.say_hello()
    print('Find the greatest common divisor of given numbers.')
    result_correct_answer = 0
    while result_correct_answer != 3:
        rand_first = random.randint(0, 100)
        rand_sec = random.randint(0, 100)
        question_nums = f'{rand_first} {rand_sec}'
        correct_answer = math.gcd(rand_first, rand_sec)
        if game_log.ask_get_check_correct_answer(question_nums, str(correct_answer)) is True:
            result_correct_answer += 1
        else:
            return 0
    print(f'Congratulations, {name}')
