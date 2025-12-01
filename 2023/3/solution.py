def sum_part_numbers(rows):
    index = 0
    previous_row = ""
    current_row = rows[0]
    next_row = rows[1]

    all_part_numbers = []
    possible_gears = {}

    while index < len(rows):
        all_part_numbers += get_part_numbers(previous_row, current_row, next_row, index, possible_gears)

        index += 1
        previous_row = current_row
        current_row = next_row

        if index < len(rows) - 1:
            next_row = rows[index + 1]
        else:
            next_row = ""

    # return sum(all_part_numbers)
    sum_of_part_numbers = sum([int(part_number) for part_number in all_part_numbers])

    # gear_ratios = [v[0] * v[1] for k, v in possible_gears if len(v) == 2]
    gear_ratios = []

    for key in possible_gears:
        if len(possible_gears[key]) == 2:
            gear_ratios.append(int(possible_gears[key][0]) * int(possible_gears[key][1]))


    return sum_of_part_numbers, sum(gear_ratios)


def get_part_numbers(previous_row, current_row, next_row, current_row_index, possible_gears):
    index = 0
    result = []

    while index < len(current_row):
        found_number = get_number(current_row[index:], "")

        if found_number:
            symbols = ["!", "*", "$", "&", "=", "-", "/", "%", "@", "#", "+"]
            if has_adjacent_symbol(previous_row,
                                   current_row,
                                   next_row,
                                   index,
                                   len(found_number),
                                   symbols,
                                   current_row_index):
                result.append(found_number)

            possible_gear_location = has_adjacent_symbol(previous_row,
                                   current_row,
                                   next_row,
                                   index,
                                   len(found_number),
                                   ["*"],
                                   current_row_index)
            if possible_gear_location:
                possible_gears[possible_gear_location] = possible_gears.get(possible_gear_location, []) + [found_number]

            index += len(found_number)
        else:
            index += 1

    return result


def get_number(string, current_number):
    if string and string[0].isdigit():
        return get_number(string[1:], current_number + string[0])
    else:
        return current_number


def has_adjacent_symbol(previous_row, current_row, next_row, start_index, size, symbols, current_row_index):
    lowest_index = start_index - 1
    highest_index = start_index + size

    if lowest_index == -1:
        lowest_index = 0

    if highest_index >= len(current_row):
        highest_index = len(current_row) - 1

    symbol_index = None

    if current_row[lowest_index] in symbols:
        symbol_index = (current_row_index, lowest_index)
    if current_row[highest_index] in symbols:
        symbol_index = (current_row_index, highest_index)

    index = lowest_index
    while index < len(previous_row) and index <= highest_index:
        if previous_row[index] in symbols:
            in_previous_row = True
            symbol_index = (current_row_index - 1, index)
            break
        index += 1

    index = lowest_index
    while index < len(next_row) and index <= highest_index:
        if next_row[index] in symbols:
            in_next_row = True
            symbol_index = (current_row_index + 1, index)
            break
        index += 1

    return symbol_index


file = open("input.txt", "r")
file_lines = file.readlines()

print(sum_part_numbers(file_lines)[0])
print(sum_part_numbers(file_lines)[1])