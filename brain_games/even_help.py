import random
import prompt


def answer_is_even(num = int):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'
    
def game_answer(name):
    res_correct_answer = 0
    while res_correct_answer != 3:
        print('Answer "yes" if the number is even, otherwise answer "no".')
        question_num = random.randint(0, 1000)
        correct_answer = answer_is_even(question_num)
        print(f'Question: {question_num}')
        answer = prompt.string('Your answer: ')
        if answer.lower() == correct_answer:
            res_correct_answer += 1
            print('Correct!')
        else:
            res_correct_answer = 0
            print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}')
    print(f'Congratulations, {name}')
    

def even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    game_answer(name)