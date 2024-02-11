import random
from . import game_log


def create_progression():
    step = random.randint(1,7)
    start = random.randint(1,50)
    progression = [start]
    for i in range (10):
        start = start + step
        progression.append(start)
    return progression

def make_correct_answer():
    progression_complete = create_progression()
    index = random.randint(0,9)
    result = progression_complete[index]
    progression_complete[index] = ".."
    return progression_complete, result

def progression_game ():
        name = game_log.say_hello()
        print('What number is missing in the progression?')
        result_correct_answer = 0
        while result_correct_answer != 3:
            question_progression, correct_answer = make_correct_answer()
            question_progression = (' '.join(map(str, question_progression)))
            if game_log.ask_get_check_correct_answer(question_progression, str(correct_answer)) is True:
                result_correct_answer += 1
            else:
                result_correct_answer = 0
        print(f'Congratulations, {name}')

