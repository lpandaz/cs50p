


# 🙂
# 🙁


# if :) then do smiley face if :( then do frowny face

def main():

    text = input("")
    new_text = convert(text)
    print(new_text)

def convert(str):
    
    new_str = str.replace(":)", "🙂")
    new_str = new_str.replace(":(", "🙁")
    return new_str

main()