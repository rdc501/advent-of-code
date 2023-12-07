from functools import reduce

if __name__ == "__main__":
    file = open("input.txt", "r")
    file_lines = file.readlines()

    # file_lines = ["Time:      7  15   30", "Distance:  9  40  200"]

    times = [int(time) for time in file_lines[0].rstrip().split(':')[1].split(' ') if time != '']
    distances = [int(distance) for distance in file_lines[1].rstrip().split(':')[1].split(' ') if distance != '']

    race_index = 0
    winning_combinations = []
    while race_index < len(times):
        seconds_attempt = 1
        winning_combination = 0
        while seconds_attempt < times[race_index]:
            if seconds_attempt * (times[race_index] - seconds_attempt) > distances[race_index]:
                winning_combination += 1
            seconds_attempt += 1

        winning_combinations.append(winning_combination)
        race_index += 1

    print(winning_combinations)
    print(reduce(lambda x, y: x*y, winning_combinations))
