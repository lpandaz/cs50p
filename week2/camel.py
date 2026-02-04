


# turn firstWords = first_words
user_input = input("camelCase: ")
new_word = ""

for letter in user_input:
    if letter.isupper() == True:
        new_word += "_"
        new_word += letter.lower()
    else:
        new_word += letter

print(new_word)