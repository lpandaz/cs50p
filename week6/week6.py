import sys
import csv

# Write to a CSV file of 


# Get one additional file prompt to write to

length = len(sys.argv)

if length > 2:
    sys.exit("Too many command line arguments")
elif length < 2:
    sys.exit("Too few command line arguments")



try:
    with open(sys.argv[1], 'a') as file:

        while True:
            name = input("What is the name? type 'd' to exit: ")
            if name == 'd':
                sys.exit("Exiting the program")
            house = input("What is their house? :")
            student = {"name": name, "house": house}
            writer = csv.DictWriter(file, fieldnames=["name", "house"])
            writer.writerow({"name": name, "house": house})
except FileNotFoundError:
    sys.exit("File doesn't exist.")




