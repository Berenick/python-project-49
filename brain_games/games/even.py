import random


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num=int):
    return True if num % 2 == 0 else False


def generate_q_a():
    question = random.randint(0, 1000)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
