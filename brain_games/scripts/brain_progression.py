import random
import sys


def generate_progression():
    begining = random.randint(1, 20)
    diff = random.randint(2, 5)
    lenght = random.randint(5, 10)
    hidden_index = random.randint(0, lenght - 1)
    progression = [begining + i * diff for i in range(lenght)]
    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'
    return " ".join(map(str, progression)), hidden_number


def run_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for _ in range(3):
        question, correct_answer = generate_progression()
        print(f"Question: {question}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return
            
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    sys.exit(run_game())
