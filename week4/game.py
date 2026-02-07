import sys
import random

while True:

    level = input("Level: ")

    if level.isdigit() == False or int(level) < 1:
        continue
    else:
        break

correct_number = random.randint(1, int(level))

while True:
    guess = input("Guess: ")

    if guess.isdigit() == True:
        guess = int(guess)
        if guess < 1:
            continue
        if guess > correct_number:
            print("Too large!")
        elif guess < correct_number:
            print("Too small!")
        else:
            sys.exit("Just right!")
    else:
        continue
