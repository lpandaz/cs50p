import sys
import csv

students = []

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row['name'].split(",")
                first = first.lstrip()
                house = row['house']
                students.append({"first": first, "last": last, "house": house})

        with open(sys.argv[2], "w", newline='') as csv_wr:
            writer = csv.DictWriter(csv_wr, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)



    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
