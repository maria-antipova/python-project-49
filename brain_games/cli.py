from prompt_toolkit import prompt


def welcome_user():
    """Welcoming message, ask name and print greeting"""
    print("Welcome to the Brain Games!")
    name = prompt("May I have your name? ")
    print(f"Hello, {name}!")
