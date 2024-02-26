import random
import math


GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num=int):
    if num <= 1:
        return False
    num_sqrt = int(math.sqrt(num))
    divisors = range(2, num_sqrt + 1)
    for elem in divisors:
        if num % elem == 0:
            return False
    return True


def generate_q_a():
    question = random.randint(1, 5000)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
