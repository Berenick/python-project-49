import game_log
import random


GAME_TASK = 'What is the result of the expression?'


def generate():
    operators = ['+', '-', '*']
    first_num = random.randint(-100, 100)
    sec_num= random.randint(-100, 100)
    rand_oper = random.choice(operators)
    question = f'{first_num} {rand_oper} {sec_num}'
    match rand_oper:
        case '+': answer = first_num + sec_num
        case '-': answer = first_num - sec_num
        case '*': answer = first_num * sec_num
    return question, str(answer)


def calc_game():
    game_log.start_game(GAME_TASK, generate)
