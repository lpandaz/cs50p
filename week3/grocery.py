

grocery_list = {}

while True:

    try:
        item = input("").lower()
    except EOFError:
        break
    else:
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

for grocery in sorted(grocery_list):
    print(f"{grocery_list[grocery]} {grocery.upper()}")
