def part_one() -> None:
    with open("./input.txt") as file:
        total = 0
        for line in file:
            _, numbers = line.split(": ")

            winning_numbers_str, numbers_str = numbers.split(" | ")
            winning_numbers = {
                int(n.strip())
                for n in winning_numbers_str.split(" ")
                if n.strip()
            }
            numbers = {
                int(n.strip()) for n in numbers_str.split(" ") if n.strip()
            }

            card_total = 0
            for n in numbers:
                if n in winning_numbers:
                    if card_total == 0:
                        card_total += 1
                    else:
                        card_total *= 2

            total += card_total
        print(total)


def part_two() -> None:
    with open("./input.txt") as file:
        lines: list[str] = file.readlines()
        total_cards: dict[int, int] = {idx: 1 for idx in range(len(lines))}

        for idx, line in enumerate(lines):
            _, numbers = line.split(": ")

            winning_numbers_str, numbers_str = numbers.split(" | ")

            winning_numbers = {
                int(n.strip())
                for n in winning_numbers_str.split(" ")
                if n.strip()
            }

            numbers = {
                int(n.strip()) for n in numbers_str.split(" ") if n.strip()
            }

            num_winning_numbers = len(winning_numbers.intersection(numbers))

            for i in range(idx + 1, idx + 1 + num_winning_numbers):
                if i not in total_cards:
                    total_cards[i] = 1
                total_cards[i] += total_cards[idx]

        print(sum(total_cards.values()))


if __name__ == "__main__":
    part_one()
    part_two()
