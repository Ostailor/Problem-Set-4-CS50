import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Names: ")
    except EOFError:
        break
    else:
        names.append(name)

print("Adieu, adieu, to " + p.join(names))
