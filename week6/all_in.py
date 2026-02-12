import csv
import sys

# This time create a new file


writing_file = input("File name and format (ex - file.csv): ")


with open(writing_file, 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writeheader()

    while True:
        status = input("Would you like to enter a pair? 'y' or 'n': ")

        if status == 'n':
            sys.exit("Exiting the program")
        elif status == 'y':
            name = input("Enter a name: ")
            house = input("Enter a house: ")
            writer.writerow({"name": name, "house": house})
        else:
            continue