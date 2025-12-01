from solution import Map, process_file


def test_map_mapping_not_known_returns_input():
    sut = Map([])

    assert sut.get(3) == 3


def test_map_mapping_known_returns_mapping():
    mapping_definitions = ["10 1 5"]
    sut = Map(mapping_definitions)

    assert sut.get(4) == 13


def test_process_file():
    file = r"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    result = process_file(file.splitlines())
    assert 79 in result
    assert 14 in result
    assert 55 in result
    assert 13 in result

    assert_result(result[79], 81, 81, 81, 74, 78, 78, 82)
    assert_result(result[14], 14, 53, 49, 42, 42, 43, 43)
    assert_result(result[55], 57, 57, 53, 46, 82, 82, 86)
    assert_result(result[13], 13, 52, 41, 34, 34, 35, 35)


def assert_result(result, soil, fertilizer, water, light, temperature, humidity, location):
    assert result.soil == soil
    assert result.fertilizer == fertilizer
    assert result.water == water
    assert result.light == light
    assert result.temperature == temperature
    assert result.humidity == humidity
    assert result.location == location
