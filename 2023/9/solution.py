def get_extrapolated_value(values):
    index = 1
    differences = []
    while index - len(values):
        differences.append(values[index] - values[index - 1])
        index += 1

    if differences.count(0) == len(differences):
        return values[-1]
    else:
        return values[-1] + get_extrapolated_value(differences)

def convert_line(line):
    values = line.split(' ')
    return [int(value) for value in values]


if __name__ == "__main__":
    file = open("input.txt", "r")
    file_lines = file.readlines()
    
    extrapolated_values = [get_extrapolated_value(convert_line(file_line)) for file_line in file_lines]
    print(sum(extrapolated_values))