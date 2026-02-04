

def main():
    print_square(3)


def print_square(size):

    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()

    # could also do this
    for x in range(size):
        print("#" * size) # then it prints a new row
main()