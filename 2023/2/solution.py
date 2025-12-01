from collections import namedtuple


def process_line(line):
    result = []
    line = line.split(":")[1]

    round_results = [round.split(",") for round in line.split(";")]

    Round = namedtuple('Round', 'red green blue')

    for round_result in round_results:
        red = 0
        green = 0
        blue = 0

        for round_value in round_result:
            number_of_cubes = round_value.split(" ")[1]

            if "red" in round_value:
                red = int(number_of_cubes)
            if "green" in round_value:
                green = int(number_of_cubes)
            if "blue" in round_value:
                blue = int(number_of_cubes)

        result.append(Round(red, green, blue))
    return result

def is_game_possible(game, max_red, max_green, max_blue):
    impossible_rounds = [round for round in game if round.red > max_red or round.green > max_green or round.blue > max_blue]

    return len(impossible_rounds) == 0

def fewest_cubes_required(game):
    Cubes = namedtuple('Cubes', 'red green blue')
    min_red = 0
    min_green = 0
    min_blue = 0

    for round in game:
        if round.red > min_red:
            min_red = round.red
        if round.green > min_green:
            min_green = round.green
        if round.blue > min_blue:
            min_blue = round.blue

    return Cubes(min_red, min_green, min_blue)



file = open("input.txt", "r")
file_lines = file.readlines()

games = []

for file_line in file_lines:
    games.append(process_line(file_line))

possible_game_indexes = [ind + 1 for ind, game in enumerate(games) if is_game_possible(game, 12, 13, 14)]

fewest_cubes = [fewest_cubes_required(game) for game in games]
fewest_cubes_powers = [cubes.red * cubes.green * cubes.blue for cubes in fewest_cubes]

print(sum(fewest_cubes_powers))