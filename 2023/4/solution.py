def parse_row(row):
    row = row.split(':')[1]
    sections = row.split('|')

    winning_numbers =  [int(number) for number in sections[0].split(' ') if number != '']
    numbers = [int(number) for number in sections[1].split(' ') if number != '']

    return winning_numbers, numbers


def get_matching_numbers(winning_numbers, numbers):
    return [number for number in numbers if number in winning_numbers]


def get_score(matching_numbers):
    match len(matching_numbers):
        case 0:
            return 0
        case 1:
            return 1

    return pow(2, len(matching_numbers) - 1)


file = open("input.txt", "r")
file_lines = file.readlines()

scores = [get_score(get_matching_numbers(*parse_row(row))) for row in file_lines]

print(sum(scores))