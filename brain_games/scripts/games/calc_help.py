from . import game_log
import random


def calc_game():
    name = game_log.say_hello()
    print('What is the result of the expression?')
    result_correct_answer = 0
    operators = ['+', '-', '*']
    while result_correct_answer != 3:
        question_sum = str(random.randint(-100, 100)) + random.choice(operators) + str(random.randint(-100, 100))
        correct_answer = str(eval(question_sum))
        if game_log.ask_get_check_correct_answer(question_sum, correct_answer, name) is True:
            result_correct_answer += 1
        else:
            return 0
    print(f'Congratulations, {name}!')
