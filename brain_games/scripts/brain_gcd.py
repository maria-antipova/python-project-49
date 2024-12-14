import random 
import math
import sys


def gcd(a, b):
    return math.gcd(a, b)


def run_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")


    for i in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = gcd(num1, num2)
        print(f"Question: {num1} {num2}")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return
    print("Congratulations!")


if __name__ == "__main__":
    run_game()
