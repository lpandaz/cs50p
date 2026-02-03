

# If 'Hello' or 'hello' 0$
# if starts with H but not hello, 20$
# anything else 100$

bonus = 0
greeting = input("Greeting: ").strip().lower()

if greeting.startswith('hello'):
    bonus = 0
elif greeting.startswith('h'):
    bonus = 20
else:
    bonus = 100

print(f"${bonus}")
