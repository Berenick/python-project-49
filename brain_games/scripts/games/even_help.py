import random
from . import game_log


GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate():
    question = random.randint(0, 1000)
    if answer_is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def answer_is_even(num=int):
    if num % 2 == 0:
        return True
    else:
        return False


def even_game():
    game_log.start_game(GAME_TASK, generate)
