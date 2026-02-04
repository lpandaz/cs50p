


# input a string with an output omitting all vowels, a e i o u case sensitive



# Input: What's your name?
# Output: Wht's yr nm?



new_string = ""
text_input = input("Input: ")

omitted_vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

for c in text_input:
    if c not in omitted_vowels:
        new_string += c

print(f"Output: {new_string}")