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

if __name__ == "__main__":
    file = open("input.txt", "r")
    file_lines = file.readlines()

    start_pipe = find_start_pipe(file_lines)

    number_of_moves = 1
    first_pipe = start_pipe[0] + 1, start_pipe[1] # Bit of a cheat from looking at the input
    location = first_pipe
    entry = (-1, 0)
    current_pipe = file_lines[location[1]][location[0]]

    while current_pipe != "S":
        move = next_pipe(current_pipe, entry)
        location = location[0] + move[0], location[1] + move[1]

        current_pipe = file_lines[location[1]][location[0]]
        entry = 0 - move[0], 0 - move[1]
        number_of_moves += 1

    print(number_of_moves)
    print(number_of_moves / 2)
