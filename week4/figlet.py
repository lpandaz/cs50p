import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

# zero cli if text random
# two cli if with font style


if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            prompt = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(prompt))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

elif len(sys.argv) == 1:
    prompt = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(prompt))

else:
    sys.exit("Invalid usage")
