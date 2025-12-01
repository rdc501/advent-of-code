def calculate(lines):
    return sum(map(calculate_line, lines))


def calculate_line(input):
    numbers = []
    index = 0

    while index < len(input):
        if input[index].isdigit():
            numbers.append(input[index])

        number_word_value = is_start_of_number_word(input[index:])

        if number_word_value:
            numbers.append(str(number_word_value))

        index += 1

    return int(numbers[0] + numbers[-1])


def is_start_of_number_word(input):
    number_words = ["one",
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine",
                    "none"]

    for number_word in number_words:
        if input.startswith(number_word):
            return map_number_word(number_word)

    return False

def map_number_word(number_word):
    match number_word:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9


file = open("input.txt", "r")
file_lines = file.readlines()

print(calculate(file_lines))
