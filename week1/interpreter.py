# x z = int
# y math symbol



expression = input("Expression: ")
x, y, z = expression.split(" ")
total = 0
x = int(x)
z = int(z)
if y == '+':
    total = x + z
elif y == '-':
    total = x - z
elif y == '*':
    total = x * z
else:
    total = x / z

print(f"{total:.1f}")