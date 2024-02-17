from . import game_log
import random
import math


def number_is_prime(num=int):
    if num == 1:
        return 'no'
    a = []
    for i in range(2, num + 1):
        a.append(i)
    for i in a:
        if i > math.sqrt(num):
            return 'yes'
        if num % i == 0:
            return 'no'


def prime_game():
    name = game_log.say_hello()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    result_correct_answer = 0
    while result_correct_answer != 3:
        question_num = random.randint(1, 5000)
        correct_answer = number_is_prime(question_num)
        if game_log.ask_get_check_correct_answer(question_num, correct_answer) is True:
            result_correct_answer += 1
        else:
            return 0
    print(f'Congratulations, {name}!')
