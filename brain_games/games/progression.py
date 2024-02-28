import random


GAME_TASK = 'What number is missing in the progression?'


def generate_round_data():
    step = random.randint(1, 7)
    start = random.randint(1, 50)
    question = list(range(start, start + step * 10, step))
    index = random.randint(0, 9)
    answer = str(question[index])
    question[index] = ".."
    question = (' '.join(map(str, question)))
    return question, answer
