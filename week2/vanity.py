#vanity license plates
# all plates MUST start with at LEAST 2 letters. so AB ABC but not A . CHECK
# vanity plates either must have a maximum of 6 characters, letters or numbers, and a minimum of 2 letters from the first two - CHECK
# numbers can't be used at the middle, must be like AB1234 or ABC222. NO AAA22A. First number used cannot be a zero.
# No periods, spaces, or punctuation marks CHECK


# first two characters must be letters
# if test_string[0:2].isalpha():
#     print("first two chars pass")
# else:
#     print("not pass")
# print(test_string[0:2])


# no periods, spaces, or punctuation marks
# if test_string.isalnum() == True:
#     print("Valid")
# else:
#     print("Invalid")


# length cant be greater than 6


# if len(test_string) > 6:
#    print("Invalid")


# Done



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    

    # returns true or false

    if len(s) < 2:
        return False

    if s.isalnum() == True and s[0:2].isalpha() == True and len(s) <= 6:
        if s[2].isnumeric() == True:
            if int(s[2]) != 0:
                if s[2:].isnumeric() == True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return True
    else:
        return False


main()