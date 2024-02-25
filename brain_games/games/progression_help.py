import random
from . import game_log


GAME_TASK = 'What number is missing in the progression?'


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
    result = str(progression_complete[index])
    progression_complete[index] = ".."
    return progression_complete, result


def generate():
    quest_progress, answer = make_correct_answer()
    question = (' '.join(map(str, quest_progress)))
    return question, answer


def progression_game():
    game_log.start_game(GAME_TASK, generate)
