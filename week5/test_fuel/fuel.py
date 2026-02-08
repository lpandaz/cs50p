def main():

    fraction_input = input("Fraction: ")
    number = convert(fraction_input)
    output = gauge(number)
    print(output)


def convert(fraction):

    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        x / y

        if x > y or x < 0 or y < 0:
            raise ValueError
    except (ValueError, ZeroDivisionError) as e:
        raise e
    else:
        return round((x/y) * 100)

def gauge(percentage):
    if percentage > 1 and percentage < 99:
        return f"{percentage}%"
    elif percentage >= 99:
        return "F"
    else:
        return "E"


if __name__ == "__main__":
    main()
