import re
import sys

'''
These formats are accepted.
Return the STR in a 24 hr format
ie 9:00 to 17:00 

Raise a ValueError if the input to convert is not these formats
Raise it if either time is invalid eg 12:60 am 13:00 pm


Someone might work late and even long works
eg 5:00 PM to 9:00 AM


9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
'''

def main():
    print(convert(input("Hours: ")))

def convert(s):
    
    check_time = re.search(r"^(\d{1,2})(:\d{2})?\s*(AM|PM)\s+to\s+(\d{1,2})(:\d{2})?\s*(AM|PM)$", s, re.IGNORECASE)

    if check_time == False:
        raise ValueError()
    
    first_hour = int(check_time.group(1))
    first_mins = check_time.group(2)

    last_hour = int(check_time.group(4))
    last_mins = check_time.group(5)

    print(first_hour, first_mins)
    print(last_hour, last_mins)

if __name__ == "__main__":
    main()