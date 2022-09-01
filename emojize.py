from emoji import emojize

while True:
    try:
        emoji = input("Input: ")
        colon = []
        for c in range(len(emoji)):
            if emoji[c] == ":":
                colon.append(c)
        if len(colon) == 0 or len(colon) % 2 == 1:
            raise ValueError
    except ValueError:
        pass
    else:
        break

if colon[0] == 0:
    print(emojize(emoji[colon[0]:colon[1]+1]))
else:
    print(emoji[:colon[0]-1] + emojize(emoji[colon[0]:colon[1]+1]))