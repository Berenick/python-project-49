import prompt


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def check_answer(question=str, cor_answer=str, name=str):
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    if answer == cor_answer:
        print('Correct!')
        return True
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {cor_answer}')
        print(f"Let's try again, {name}!")
        return False


def start_game(GAME_TASK, generate):
    name = say_hello()
    print(GAME_TASK)
    for i in range(3):
        question, answer = generate()
        boolean = check_answer(question, answer, name)
        if boolean is False:
            exit()
    print(f'Congratulations, {name}!')
