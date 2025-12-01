def sum_part_numbers(rows):
    index = 0
    previous_row = ""
    current_row = rows[0]
    next_row = rows[1]

    all_part_numbers = []

    while index < len(rows):
        all_part_numbers += get_part_numbers(previous_row, current_row, next_row)

        index += 1
        previous_row = current_row
        current_row = next_row

        if index < len(rows) - 1:
            next_row = rows[index + 1]
        else:
            next_row = ""

    # return sum(all_part_numbers)
    return sum([int(part_number) for part_number in all_part_numbers])
def get_part_numbers(previous_row, current_row, next_row):
    index = 0
    result = []

    while index < len(current_row):
        found_number = get_number(current_row[index:], "")

        if found_number:
            if has_adjacent_symbol(previous_row, current_row, next_row, index, len(found_number)):
                result.append(found_number)

            index += len(found_number)
        else:
            index += 1

    return result


def get_number(string, current_number):
    if string and string[0].isdigit():
        return get_number(string[1:], current_number + string[0])
    else:
        return current_number


def has_adjacent_symbol(previous_row, current_row, next_row, start_index, size):
    lowest_index = start_index - 1
    highest_index = start_index + size

    if lowest_index == -1:
        lowest_index = 0

    if highest_index >= len(current_row):
        highest_index = len(current_row) - 1

    in_current_row = is_symbol(current_row[lowest_index]) or is_symbol(current_row[highest_index])
    in_previous_row = False
    in_next_row = False

    index = lowest_index
    while index < len(previous_row) and index <= highest_index:
        if is_symbol(previous_row[index]):
            in_previous_row = True
            break
        index += 1

    index = lowest_index
    while index < len(next_row) and index <= highest_index:
        if is_symbol(next_row[index]):
            in_next_row = True
            break
        index += 1



    return in_current_row or in_previous_row or in_next_row

def is_symbol(char):
    symbols = ["!", "*", "$", "&", "=", "-", "/", "%", "@", "#", "+"]

    return char in symbols


file = open("input.txt", "r")
file_lines = file.readlines()

print(sum_part_numbers(file_lines))