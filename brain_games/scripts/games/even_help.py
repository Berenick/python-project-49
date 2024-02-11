import random
from . import game_log


def answer_is_even(num = int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
    
def even_game():
        name = game_log.say_hello()
        print('Answer "yes" if the number is even, otherwise answer "no".')
        result_correct_answer = 0
        while result_correct_answer != 3:
            question_num = random.randint(0, 1000)
            correct_answer = answer_is_even(question_num)
            if game_log.ask_get_check_correct_answer(question_num, correct_answer) is True:
                result_correct_answer += 1
            else:
                return 0
        print(f'Congratulations, {name}')
    


