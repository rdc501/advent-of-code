def can_move_to_pipe(pipe, location):
    match pipe:
        case "|":
            return location[0] == 0
        case "-":
            return location[1] == 0
        case "L":
            return location == (0, 1) or location == (-1, 0)
        case "J":
            return location == (0, 1) or location == (1, 0)
        case "7":
            return location == (0, -1) or location == (1, 0)
        case "F":
            return location == (0, -1) or location == (-1, 0)
        case ".":
            return False
        case "S":
            return True


def next_pipe(pipe, entry):
    match pipe, entry:
        case "|", (0, -1):
            return 0, 1
        case "|", (0, 1):
            return 0, -1
        case "-", (-1, 0):
            return 1, 0
        case "-", (1, 0):
            return -1, 0
        case "L", (0, -1):
            return 1, 0
        case "L", (1, 0):
            return 0, -1
        case "J", (0, -1):
            return -1, 0
        case "J", (-1, 0):
            return 0, -1
        case "7", (-1, 0):
            return 0, 1
        case "7", (0, 1):
            return -1, 0
        case "F", (1, 0):
            return 0, 1
        case "F", (0, 1):
            return 1, 0


def find_start_pipe(rows):
    row_index = 0
    while row_index < len(rows):
        column_index = rows[row_index].find("S")

        if column_index != -1:
            return column_index, row_index

        row_index += 1

def get_route(rows, start_pipe):
    route = []
    number_of_moves = 1
    first_pipe = start_pipe[0] + 1, start_pipe[1] # Bit of a cheat from looking at the input
    # first_pipe = start_pipe[0], start_pipe[1] + 1 # Bit of a cheat from looking at the input
    location = first_pipe
    entry = (-1, 0)
    # entry = (0, -1)
    current_pipe = rows[location[1]][location[0]]

    route.append((start_pipe[1], start_pipe[0]))

    while current_pipe != "S":
        route.append((location[1], location[0]))
        move = next_pipe(current_pipe, entry)
        location = location[0] + move[0], location[1] + move[1]

        current_pipe = rows[location[1]][location[0]]
        entry = 0 - move[0], 0 - move[1]
        number_of_moves += 1

    return route


def get_potential_enclosed_tiles(rows, route):
    tiles = []
    row_index = 0
    while row_index < len(rows):
        column_index = 0
        new_row = ""
        while column_index < len(rows[row_index]):
            if (row_index, column_index) in route:
                new_row += rows[row_index][column_index]
            else:
                new_row += "?"
            column_index += 1
        tiles.append(new_row)
        row_index += 1

    return tiles


def exclude_tiles_connected_to_edge(rows):
    tiles = []
    row_index = 0
    change_made = False
    while row_index < len(rows):
        column_index = 0
        new_row = ""
        while column_index < len(rows[row_index]):
            if rows[row_index][column_index] == "?" or rows[row_index][column_index] == "o":
                if row_index == 0 or column_index == 0:
                    new_row += "."
                    change_made = True
                elif row_index == len(rows) - 1 or column_index == len(rows[row_index]) - 1:
                    new_row += "."
                    change_made = True
                elif tiles[row_index - 1][column_index] == ".":
                    new_row += "."
                    change_made = True
                elif new_row[-1] == ".":
                    new_row += "."
                    change_made = True
                else:
                    new_row += rows[row_index][column_index]
            else:
                new_row += rows[row_index][column_index]
            column_index += 1
        row_index += 1
        tiles.append(new_row)
    return (tiles, change_made)


def flip_reverse_rows(rows):
    return list(reversed([row[::-1] for row in rows]))


def expand_rows(rows):
    new_rows = ["o".join(list(row)) for row in rows]

    row_index = 0
    while row_index < len(new_rows):
        column_index = 1
        while column_index < len(new_rows[row_index]):
            if new_rows[row_index][column_index] == "S":
                new_rows[row_index] = new_rows[row_index][:column_index] + "-" + new_rows[row_index][column_index + 1:]
            if new_rows[row_index][column_index] == "o":
                if new_rows[row_index][column_index - 1] == ".":
                    new_rows[row_index] = new_rows[row_index][:column_index] + "." + new_rows[row_index][column_index + 1:]
                elif new_rows[row_index][column_index - 1] == "-" or \
                   new_rows[row_index][column_index - 1] == "F" or \
                   new_rows[row_index][column_index - 1] == "L":
                    new_rows[row_index] = new_rows[row_index][:column_index] + "-" + new_rows[row_index][column_index + 1:]
            column_index += 1
        row_index += 1

    result = []
    for row in new_rows:
        result.append(row)
        new_row = []
        index = 0
        while index < len(row):
            match row[index]:
                case ".":
                    new_row.append(".")
                case "|":
                    new_row.append("|")
                case "F":
                    new_row.append("|")
                case "7":
                    new_row.append("|")
                case _:
                    new_row.append("o")
            index += 1
        result.append("".join(new_row))

    return result


def process_lines(rows):
    start_pipe = find_start_pipe(rows)
    route = get_route(rows, start_pipe)

    print(len(route))
    print(len(route) / 2)

    potential_enclosed_tiles = get_potential_enclosed_tiles(rows, route)
    # for row in potential_enclosed_tiles:
    #     print(row)
    potential_enclosed_tiles = exclude_tiles_connected_to_edge(potential_enclosed_tiles)[0]

    potential_enclosed_tiles = exclude_tiles_connected_to_edge(flip_reverse_rows(potential_enclosed_tiles))[0]
    potential_enclosed_tiles = flip_reverse_rows(potential_enclosed_tiles)

    expanded_rows = expand_rows(potential_enclosed_tiles)
    # for row in expanded_rows:
    #     print(row)

    changes_made = True
    while changes_made:
        expanded_rows, changes_made = exclude_tiles_connected_to_edge(flip_reverse_rows(expanded_rows))

    for row in flip_reverse_rows(expanded_rows):
        print(row)

    print("".join(expanded_rows).count("?"))


if __name__ == "__main__":
    file = open("input.txt", "r")
    file_lines = file.readlines()

    process_lines(file_lines)