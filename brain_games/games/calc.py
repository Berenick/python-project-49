import random


GAME_TASK = 'What is the result of the expression?'


def generate_round_data():
    operators = ['+', '-', '*']
    first_num = random.randint(-100, 100)
    second_num = random.randint(-100, 100)
    random_oper = random.choice(operators)
    question = f'{first_num} {random_oper} {second_num}'
    match random_oper:
        case '+': answer = first_num + second_num
        case '-': answer = first_num - second_num
        case '*': answer = first_num * second_num
    return question, str(answer)
