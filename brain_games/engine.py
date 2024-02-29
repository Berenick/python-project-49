import prompt


ROUNDS_COUNT = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_TASK)
    for i in range(ROUNDS_COUNT):
        question, correct_answer = game.generate_round_data()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        if answer != correct_answer:
            print(f'{answer} is wrong answer ;(.'
                  f'Correct answer was {correct_answer}')
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
