import random


GAME_TASK = 'What number is missing in the progression?'


def create_progression():
    step = random.randint(1, 7)
    start = random.randint(1, 50)
    progression = list(range(start, start + step * 10, step))
    return progression


def make_correct_answer():
    progression_complete = create_progression()
    index = random.randint(0, 9)
    result = str(progression_complete[index])
    progression_complete[index] = ".."
    return progression_complete, result


def generate_q_a():
    question = create_progression()
    index = random.randint(0, 9)
    answer = str(question[index])
    question[index] = ".."
    question = (' '.join(map(str, question)))
    return question, answer
