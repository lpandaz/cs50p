


# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue # continue to stay within this loop
#     else:
#         break # break out of this loop if n is greater than 0


# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

def main():
    
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

main()