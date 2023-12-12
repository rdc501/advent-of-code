# import itertools
import more_itertools


def is_match(input, pattern):
    chains = [int(n) for n in pattern.split(",")]

    if input.count("#") != sum(chains):
        return False

    found_chains = [chain for chain in input.split(".") if chain != ""]

    if len(chains) != len(found_chains):
        return False

    chain_index = 0
    while chain_index < len(chains):
        if chains[chain_index] != len(found_chains[chain_index]):
            return False
        chain_index += 1

    return True


def create_combinations(input, pattern):
    number_broken = sum([int(n) for n in pattern.split(",")])
    known_broken = input.count("#")

    unknown_broken = number_broken - known_broken

    slots = input.count("?")

    items = ["#"] * unknown_broken + ["."] * (slots - unknown_broken)

    valid_combinations = []
    for slot_combination in more_itertools.distinct_permutations(items, slots):
        combination = create_potential_combination(input, slot_combination)
        if is_match(combination, pattern):
            valid_combinations.append(combination)

    return valid_combinations


def create_potential_combination(input, values):
    input_list = list(input)

    index = 0
    value_index = 0
    while index < len(input_list):
        if input_list[index] == "?":
            input_list[index] = values[value_index]
            value_index += 1
        index += 1

    return "".join(input_list)


def unfold(row):
    input = row.split(" ")[0]
    pattern = row.split(" ")[1]

    return "?".join([input] * 5),  ",".join([pattern] * 5)


if __name__ == "__main__":
    file = open("input.txt", "r")
    file_lines = file.readlines()

    row_index = 1
    combinations = []
    for row in file_lines:
        # input = row.split(" ")[0]
        # pattern = row.split(" ")[1]
        input, pattern = unfold(row)
        print(row_index)
        combinations.append(create_combinations(input, pattern))
        row_index += 1

    print(sum([len(c) for c in combinations]))