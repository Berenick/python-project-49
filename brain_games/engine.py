import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_TASK)
    for i in range(3):
        question, c_answer = game.generate_q_a()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == c_answer:
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {c_answer}')
            print(f"Let's try again, {name}!")
            exit()
    print(f'Congratulations, {name}!')
