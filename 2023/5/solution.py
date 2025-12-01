from collections import namedtuple


class Map:
    def __init__(self, mapping_definitions):
        # mappings = {}
        mappings = []

        for definition in mapping_definitions:
            mappings = self.add_mappings(mappings, definition)

        self.mappings = mappings

    def get(self, input):
        result = input
        for mapping in self.mappings:
            if input < mapping.source_start:
                break

            if input < mapping.source_start + mapping.range:
                result = mapping.destination_start + (input - mapping.source_start)
                break

        return result

    def add_mappings(self, mappings, definition):
        parsed_definition = [int(value) for value in definition.split(' ')]
        destination_start = parsed_definition[0]
        source_start = parsed_definition[1]
        range_length = parsed_definition[2]

        Mapping = namedtuple("Mapping", "source_start range destination_start")
        mappings.append(Mapping(source_start, range_length, destination_start))

        def mapping_sort(mapping):
            return mapping.source_start

        mappings.sort(key=mapping_sort)

        return mappings



def process_file(file_lines):
    Result = namedtuple("Result", "soil fertilizer water light temperature humidity location")
    result = {}

    seeds = get_seeds(file_lines[0])
    definitions = get_mapping_definitions(file_lines[3:])

    soil_map = Map(definitions[0])
    fertilizer_map = Map(definitions[1])
    water_map = Map(definitions[2])
    light_map = Map(definitions[3])
    temperature_map = Map(definitions[4])
    humidity_map = Map(definitions[5])
    location_map = Map(definitions[6])

    for seed in seeds:
        soil = soil_map.get(seed)
        fertilizer = fertilizer_map.get(soil)
        water = water_map.get(fertilizer)
        light = light_map.get(water)
        temperature = temperature_map.get(light)
        humidity = humidity_map.get(temperature)
        location = location_map.get(humidity)

        result[seed] = Result(soil,
                              fertilizer,
                              water,
                              light,
                              temperature,
                              humidity,
                              location)

    return result

def get_seeds(seed_line):
    seeds = seed_line.split(":")[1].split(' ')
    return [int(seed) for seed in seeds if seed != '']

def get_mapping_definitions(file_lines):
    soil_definitions = []
    fertilizer_definitions = []
    water_definitions = []
    light_definitions = []
    temperature_definitions = []
    humidity_definitions = []
    location_definitions = []

    index = 0
    while file_lines[index] != "soil-to-fertilizer map:":
        if file_lines[index] != '':
            soil_definitions.append(file_lines[index])

        index += 1

    index += 1

    while file_lines[index] != "fertilizer-to-water map:":
        if file_lines[index] != '':
            fertilizer_definitions.append(file_lines[index])

        index += 1

    index += 1

    while file_lines[index] != "water-to-light map:":
        if file_lines[index] != '':
            water_definitions.append(file_lines[index])

        index += 1

    index += 1

    while file_lines[index] != "light-to-temperature map:":
        if file_lines[index] != '':
            light_definitions.append(file_lines[index])

        index += 1

    index += 1

    while file_lines[index] != "temperature-to-humidity map:":
        if file_lines[index] != '':
            temperature_definitions.append(file_lines[index])

        index += 1

    index += 1

    while file_lines[index] != "humidity-to-location map:":
        if file_lines[index] != '':
            humidity_definitions.append(file_lines[index])

        index += 1

    index += 1

    while index < len(file_lines):
        location_definitions.append(file_lines[index])

        index += 1

    return (soil_definitions,
            fertilizer_definitions,
            water_definitions,
            light_definitions,
            temperature_definitions,
            humidity_definitions,
            location_definitions)


file = open("input.txt", "r")
file_lines = file.readlines()
file_lines = [line.rstrip() for line in file_lines]

result = process_file(file_lines)

lowest_location = None

for key in result:
    if lowest_location == None or result[key].location < lowest_location:
        lowest_location = result[key].location

print(lowest_location)