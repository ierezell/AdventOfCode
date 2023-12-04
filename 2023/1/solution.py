def part_one() -> None:
    with open("./input.txt") as file:
        total: int = 0
        for line in file:
            numbers: list[str] = []
            for character in line:
                if character.isdigit():
                    numbers.append(character)
            total += int(numbers[0] + numbers[-1])
        print(total)


def part_two() -> None:
    word_to_digit = {
        "zero": "ze0o",
        "one": "o1e",
        "two": "t2o",
        "three": "thr3e",
        "four": "fo4r",
        "five": "fi5e",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ht",
        "nine": "n9ne",
    }

    with open("./input.txt") as file:
        total: int = 0
        for line in file:
            digit_only_line = line
            for word, value in word_to_digit.items():
                if word in line:
                    digit_only_line = digit_only_line.replace(word, value)

            numbers: list[str] = []
            for character in digit_only_line:
                if character.isdigit():
                    numbers.append(character)
            total += int(numbers[0] + numbers[-1])
        print(total)


if __name__ == "__main__":
    part_one()
    part_two()
