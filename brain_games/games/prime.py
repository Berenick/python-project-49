import random
import math


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num=int):
    if num == 1:
        return False
    for i in range(2, math.sqrt(num)):
        if num % i == 0:
            return False
        else:
            return True


def generate_q_a():
    question = random.randint(1, 5000)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
