def part_one() -> None:
    max_colors = {"red": 12, "green": 13, "blue": 14}

    with open("./input.txt") as file:
        total = 0
        for line in file:
            game_id_str, all_games = line.split(":")
            game_id = int(game_id_str.replace("Game ", "").strip())

            passing = True
            for game in all_games.split(";"):
                for number_color in game.split(","):
                    number, color = number_color.strip().split(" ")
                    if int(number) > max_colors[color]:
                        passing = False

            if passing:
                total += game_id

        print(total)


def part_two() -> None:
    with open("./input.txt") as file:
        total = 0
        for line in file:
            _, all_games = line.split(":")

            min_set = {"red": 0, "green": 0, "blue": 0}
            for game in all_games.split(";"):
                for number_color in game.split(","):
                    number, color = number_color.strip().split(" ")

                    min_set[color] = max(min_set[color], int(number))

            total += min_set["red"] * min_set["green"] * min_set["blue"]

        print(total)


if __name__ == "__main__":
    part_one()
    part_two()
