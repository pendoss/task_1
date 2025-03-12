import random


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


def play_game():
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    
    print("\nWhat number is missing in the progression?")

    for _ in range(3):
        progression = generate_progression()
        progression, correct_answer = hide_number(progression)
        
        print(f"\nQuestion: {' '.join(map(str, progression))}")
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