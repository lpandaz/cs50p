import emoji

prompt = input("Output: ")

prompt = emoji.emojize(prompt, language="alias")
print(prompt)
