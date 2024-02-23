from . import game_log
import random
import math


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def number_is_prime(num=int):
    if num == 1:
        return 'no'
    a = []
    for i in range(2, num + 1):
        a.append(i)
    for i in a:
        if i > math.sqrt(num):
            return True
        if num % i == 0:
            return False


def generate():
    question = random.randint(1, 5000)
    if number_is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer


def prime_game():
    game_log.start_game(GAME_TASK, generate)
