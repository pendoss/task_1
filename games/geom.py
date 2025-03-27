import random


def geom_game():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    
    progression = [start]

    for i in range(1, length):
        progression.append(progression[-1] * ratio)

    hidden_pos = random.randint(0, len(progression) - 1)
    answer = progression[hidden_pos]
    progression[hidden_pos] = '..'
    return progression, answer
