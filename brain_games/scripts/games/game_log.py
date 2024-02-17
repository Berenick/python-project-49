import prompt


def say_hello():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def pr_question(question):
    print(f'Question: {question}')


def ask_get_check_correct_answer(question=str, correct_answer=str):
    pr_question(question)
    answer = get_answer()
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {correct_answer}')
        return False
