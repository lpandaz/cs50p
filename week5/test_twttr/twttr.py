

def main():

    input_word = input("Input: ")
    new_word = shorten(input_word)
    print(new_word)

def shorten(word):
    new_string = ""
    omitted_vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    for c in word:
        if c not in omitted_vowels:
            new_string += c
    
    return new_string

if __name__ == "__main__":
    main()