def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
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

if __name__ == "__main__":
    main()