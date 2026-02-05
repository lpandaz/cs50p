



# ask the user for x/y where x is a non negative integer and y is a positive integer and then outputs it to the nearest percent rounded to the nearest integer
# if <= 1 then output E if 99% or more than output F

# so 3/4 = 75%
# 4/4 = F
# 0/4 = E

# All errors should be reprompted, 4/0 = ZeroDivisionError
# three/four = valueError
# 1.5/3 valueerror
# -3/4 valueError
# 5/4 rempropt


def main():

    while True:
        fraction_input = input("Fraction: ")
        try:
            x, y = fraction_input.split("/")
            x, y = int(x), int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x > y or x < 0 or y < 0:
                pass
            else:
                break

    number = do_division(x, y)

    if number > 1 and number < 99:
        print(f"{number}%")
    elif number >= 99:
        print("F")
    else:
        print("E")

def do_division(a, b):
    percent_number = (a/b) * 100
    percent_number = round(percent_number)
    return percent_number


main()
