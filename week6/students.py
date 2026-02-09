import csv
# this is a test < -- this doesn't count
'''
this is a test
'''
 # why does this count
name = input("Whats your name? ")
home = input("Whats your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})


# test
# test two
 # test trhee