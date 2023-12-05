def part_one() -> None:
    with open("./input.txt") as file:
        symbols_mask: set[tuple[int, int]] = set()
        number_positions: list[tuple[int, set[tuple[int, int]]]] = []

        current_num_pos: set[tuple[int, int]] = set()
        current_num_str: str = ""
        for y, line in enumerate(file):
            if current_num_pos:
                number_positions.append(
                    (int(current_num_str), current_num_pos),
                )
                current_num_pos = set()
                current_num_str = ""

            for x, char in enumerate(line.strip()):
                if not char.isdecimal() and char != ".":
                    print(repr(char))
                    symbols_mask.add((x - 1, y + 1))
                    symbols_mask.add((x, y + 1))
                    symbols_mask.add((x + 1, y + 1))
                    symbols_mask.add((x - 1, y))
                    symbols_mask.add((x, y))
                    symbols_mask.add((x + 1, y))
                    symbols_mask.add((x - 1, y - 1))
                    symbols_mask.add((x, y - 1))
                    symbols_mask.add((x + 1, y - 1))

                if (not char.isdecimal()) and current_num_pos:
                    number_positions.append(
                        (int(current_num_str), current_num_pos),
                    )
                    current_num_pos = set()
                    current_num_str = ""

                if char.isdecimal():
                    current_num_pos.add((x, y))
                    current_num_str += char

        if current_num_pos:
            number_positions.append((int(current_num_str), current_num_pos))

        total = 0
        for number, positions in number_positions:
            if symbols_mask.intersection(positions):
                total += number

        print(total)


def part_two() -> None:
    with open("./input.txt") as file:
        symbols_mask: list[set[tuple[int, int]]] = []
        number_positions: list[tuple[int, set[tuple[int, int]]]] = []

        current_num_pos: set[tuple[int, int]] = set()
        current_num_str: str = ""
        for y, line in enumerate(file):
            if current_num_pos:
                number_positions.append(
                    (int(current_num_str), current_num_pos),
                )
                current_num_pos = set()
                current_num_str = ""

            for x, char in enumerate(line):
                if char.isdecimal():
                    current_num_pos.add((x, y))
                    current_num_str += char

                if (not char.isdecimal()) and current_num_pos:
                    number_positions.append(
                        (int(current_num_str), current_num_pos),
                    )
                    current_num_pos = set()
                    current_num_str = ""

                if char == "*":
                    gear: set[tuple[int, int]] = set()
                    gear.add((x - 1, y + 1))
                    gear.add((x, y + 1))
                    gear.add((x + 1, y + 1))
                    gear.add((x - 1, y))
                    gear.add((x, y))
                    gear.add((x + 1, y))
                    gear.add((x - 1, y - 1))
                    gear.add((x, y - 1))
                    gear.add((x + 1, y - 1))
                    symbols_mask.append(gear)

        if current_num_pos:
            number_positions.append((int(current_num_str), current_num_pos))

        total = 0
        for gear in symbols_mask:
            gear_touches: list[int] = []
            for number, positions in number_positions:
                if gear.intersection(positions):
                    gear_touches.append(number)

            num_gear_number = 2
            if len(gear_touches) == num_gear_number:
                total += gear_touches[0] * gear_touches[1]

        print(total)


if __name__ == "__main__":
    part_one()
    part_two()
