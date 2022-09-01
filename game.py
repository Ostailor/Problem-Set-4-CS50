import random

while True:
    try:
        b = int(input("Level: "))
        if b <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        break

correct = random.randint(1, b)


while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        if guess > correct:
            print("Too large!")
        elif guess == correct:
            print("Just right!")
            break
        else:
            print("Too small!")
