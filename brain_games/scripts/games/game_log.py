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


def check_answer(question=str, cor_answer=str, name=str):
    pr_question(question)
    answer = get_answer()
    if answer == cor_answer:
        print('Correct!')
        return True
    else:
        print(f'{answer} is wrong answer ;(. Correct answer was {cor_answer}')
        print(f"Let's try again, {name}!")
        return False
