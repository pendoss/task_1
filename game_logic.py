import random
from functools import reduce
from math import gcd

from games.geom import geom_game
from games.NOK import nok


def generate_progression():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    
    progression = [start]
    for i in range(1, length):
        progression.append(progression[-1] * ratio)
    
    return progression


def hide_number(progression):
    hidden_pos = random.randint(0, len(progression) - 1)
    answer = progression[hidden_pos]
    progression[hidden_pos] = '..'
    return progression, answer


def lcm(a, b):
    
    return abs(a * b) // gcd(a, b)


def lcm_of_three(numbers):
    return reduce(lcm, numbers)


def generate_numbers():
    return [random.randint(1, 100) for _ in range(3)]


def play_game(game_name):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    if game_name == "nok":
        print("\nFind the smallest common multiple of given numbers.")
        game_function = nok
    elif game_name == "geom":
        print("\nWhat number is missing in the progression?")
        game_function = geom_game
    else:
        print(f"Unknown game: {game_name}")
        return

    for _ in range(3):
        numbers, correct_answer = game_function()
        
        if game_name == "nok":
            print(f"\nQuestion: {' '.join(map(str, numbers))}")
        else:
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
    import sys
    
    if len(sys.argv) > 1:
        game_choice = sys.argv[1]
    else:
        game_choice = input("Choose a game (nok/geom): ")
    
    play_game(game_choice)