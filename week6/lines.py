import sys

count = 0
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif sys.argv[1].endswith('.py') == False:
    sys.exit("Not a python file.")
else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith("#") == False and line.isspace() == False:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        print(count)
