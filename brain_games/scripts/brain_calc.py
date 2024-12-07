import random
import operator
import sys

OPS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
}


def generate_expression():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    op = random.choice(list(OPS.keys()))
    expression = f"{num1} {op} {num2}"
    result = OPS[op](num1, num2)
    return expression, result



def run_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")


    for i in range(3):
        expression, correct_answer = generate_expression()
        print(f"Question: {expression}")
        try:
            user_answer = int(input("your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
            else:
                print(f"'{user_answer}' is wrong answer:(. Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return 0
        except ValueError:
            print("Invalid input. Please enter an ineger.")
            return 0
    print(f"Congatulations, {name}!")


if __name__ == "__main__":
    sys.exit(run_game())
