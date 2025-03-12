import random
from functools import reduce
from math import gcd


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def lcm_of_three(numbers):
    return reduce(lcm, numbers)


def generate_numbers():
    return [random.randint(1, 100) for _ in range(3)]


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("\nFind the smallest common multiple of given numbers.")

    for _ in range(3):
        numbers = generate_numbers()
        correct_answer = lcm_of_three(numbers)
        
        print(f"\nQuestion: {' '.join(map(str, numbers))}")
        user_answer = input("Your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"\nCongratulations, {name}!")


if __name__ == "__main__":
    play_game()