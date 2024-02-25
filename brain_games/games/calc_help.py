from . import game_log
import random


GAME_TASK = 'What is the result of the expression?'


def generate():
    operators = ['+', '-', '*']
    first_num_of_exp = str(random.randint(-100, 100))
    sec_num_of_exp = str(random.randint(-100, 100))
    rand_oper = random.choice(operators)
    question_sum = f'{first_num_of_exp} {rand_oper} {sec_num_of_exp}'
    correct_answer = str(eval(question_sum))
    return question_sum, correct_answer


def calc_game():
    game_log.start_game(GAME_TASK, generate)
