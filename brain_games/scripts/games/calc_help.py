from . import game_log
import random


def calc_game():
    name = game_log.say_hello()
    print('What is the result of the expression?')
    result_correct_answer = 0
    operators = ['+', '-', '*']
    while result_correct_answer != 3:
        first_rannum_of_exp = str(random.randint(-100, 100))
        sec_rannum_of_exp = str(random.randint(-100, 100))
        rand_oper = random.choice(operators)
        question_sum = f'{first_rannum_of_exp} {rand_oper} {sec_rannum_of_exp}'
        correct_answer = str(eval(question_sum))
        if game_log.check_correct_answer(question_sum, correct_answer, name) is True:
            result_correct_answer += 1
        else:
            return 0
    print(f'Congratulations, {name}!')
