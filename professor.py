import random


def main():
    i = 0
    correct = 0

    y = get_level()
    while i < 10:
        incorrect_tries = 0
        value_errors = 0
        one = generate_integer(y)
        two = generate_integer(y)
        while value_errors != 3 and incorrect_tries <= 2:
            try:
                answer = int(input(f"{one} + {two} = "))
            except ValueError:
                value_errors += 1
                incorrect_tries += 1
                print("EEE")
            else:
                break
        errors = 0
        while errors != 2 and incorrect_tries <= 2 and value_errors != 3:
            if answer != one + two:
                print("EEE")
                print(incorrect_tries, value_errors, errors)
                answer = int(input(f"{one} + {two} = "))
                errors += 1
                incorrect_tries += 1
            else:
                break
        if errors == 0 and incorrect_tries == 0 and value_errors == 0:
            correct += 1
        if incorrect_tries == 2 or value_errors == 3:
            print(f"{one} + {two} = {one + two}")
        i += 1
    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            pass
        else:
            return x


def generate_integer(level):
    if level == 1:
        range_start = 10 ** (level - 1) - 1
    else:
        range_start = 10 ** (level - 1)
    range_end = (10 ** level) - 1
    return random.randint(range_start, range_end)


if __name__ == "__main__":
    main()
