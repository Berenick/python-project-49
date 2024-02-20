import random
from . import game_log


def create_progression():
    step = random.randint(1, 7)
    start = random.randint(1, 50)
    progression = [start]
    for i in range(10):
        start = start + step
        progression.append(start)
    return progression


def make_correct_answer():
    progression_complete = create_progression()
    index = random.randint(0, 9)
    result = progression_complete[index]
    progression_complete[index] = ".."
    return progression_complete, result


def progression_game():
    name = game_log.say_hello()
    print('What number is missing in the progression?')
    result_correct_answer = 0
    while result_correct_answer != 3:
        quest_progress, cor_answ = make_correct_answer()
        quest_progress = (' '.join(map(str, quest_progress)))
        if game_log.check_answer(quest_progress, str(cor_answ), name) is True:
            result_correct_answer += 1
        else:
            return 0
    print(f'Congratulations, {name}!')
