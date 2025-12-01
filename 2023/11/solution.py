def expand_universe(universe):
    new_universe = []
    columns_with_galaxies = {}

    row_index = 0
    while row_index < len(universe):
        column_index = 0
        if universe[row_index].find("#") == -1:
            new_universe.append("." * len(universe[row_index]))
        while column_index < len(universe[row_index]):
            if universe[row_index][column_index] == "#":
                columns_with_galaxies[column_index] = True
            column_index += 1
        new_universe.append(universe[row_index])
        row_index += 1

    row_index = 0
    while row_index < len(new_universe):
        column_index = len(new_universe[row_index]) - 1
        while column_index >= 0:
            if not columns_with_galaxies.get(column_index, False):
                new_universe[row_index] = new_universe[row_index][:column_index] + "." + new_universe[row_index][column_index:]
            column_index -= 1
        row_index += 1

    return new_universe


def find_galaxies(universe):
    galaxies = {}

    row_index = 0
    while row_index < len(universe):
        column_index = 0
        while column_index < len(universe[row_index]):
            if universe[row_index][column_index] == "#":
                galaxies[(row_index, column_index)] = []
            column_index += 1
        row_index += 1

    return galaxies


def find_distances(galaxies):
    for start_location in galaxies:
        for end_location in galaxies:
            if start_location != end_location and len(galaxies[end_location]) == 0:
                distance = abs(end_location[0] - start_location[0]) + abs(end_location[1] - start_location[1])
                galaxies[start_location].append(distance)

    return galaxies


if __name__ == "__main__":
    file = open("input.txt", "r")
    file_lines = file.readlines()

    distances = find_distances(find_galaxies(expand_universe(file_lines)))

    print(sum(sum([value for key, value in distances.items()], [])))
