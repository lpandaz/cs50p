import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    first_search = re.search(r"^<iframe (\w)+> </iframe>$",s)
    if first_search:
        return True
    else:
        return False

...


if __name__ == "__main__":
    main()