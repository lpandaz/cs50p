import random


def main():


    level = get_level()


    # generate problems which are additions
    problems = 0
    score = 0
    while problems < 10: #just do it 3 times for now
        guesses = 0
        x = generate_integer(level)
        y = generate_integer(level)

        while guesses < 3:

            guess_answer = input(f"{x} + {y} = ")

            if guess_answer.isdigit() == False:
                guesses += 1
                print("EEE")
                continue
            elif int(guess_answer) != x + y:
                if guesses == 2:
                    print(f"{x} + {y} = {x+y}")
                    break
                else:
                    guesses += 1
                    print("EEE")
                    continue
            elif int(guess_answer) == x + y:
                score += 1
                break

        problems += 1

    print(f"Score: {score}")

def get_level():
    while True:
        n = input("Level: ")
        if n != '1' and n != '2' and n != '3':
            continue
        else:
            break

    return int(n)


def generate_integer(level):

    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    elif level == 3:
        return random.randrange(100, 1000)


if __name__ == "__main__":
    main()
