from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
elif len(sys.argv) == 2 or len(sys.argv) > 3:
    print("Invalid Usage")
    sys.exit()
elif sys.argv[1] not in ["-f", "--font"]:
    print("Invalid Usage")
    sys.exit()
elif sys.argv[2] not in figlet.getFonts():
    print("Invalid Usage")
    sys.exit()
else:
    figlet.setFont(font=sys.argv[2])

s = input("Input: ")

print(figlet.renderText(s))
