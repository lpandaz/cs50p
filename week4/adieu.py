# if one name, no and and no comma
# if two names, n comma and just one and. mark and yeza
# if three names or more, n comma per name. Liesel, Fred, and Mark
import inflect
p = inflect.engine()

greetings = "Adieu, adieu, to "
names = []
while True:

    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        names.append(name)


# control check


greetings += p.join((names))
print(greetings)
