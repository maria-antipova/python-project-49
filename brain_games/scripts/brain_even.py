import random
from prompt_toolkit import prompt


def is_even(number):
    return number % 2 == 0


def get_answer(number):
    print(f"Question: {number}")
    answer = prompt("Your answer: ").lower()
    return answer


def run_game():
    print("Welcome to the Brain Games!")
    name = prompt("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')


    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        correct_answer = "yes" if is_even(number) else "no"
        user_answer = get_answer(number)


        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return


    print(f"Congratulations, {name}!")


if __name__ == "__name__":
    run_game()
