import re
import sys



'''
accept a format of
#.#.#.#. but each # should be between 0 and 255 inclusive
'''

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    

    matches = re.search(r"^(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", ip, re.IGNORECASE)
    if matches:
        return True
    else:
        return False



if __name__ == "__main__":
    main()