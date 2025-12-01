import pytest
from solution import get_part_numbers, sum_part_numbers


@pytest.mark.parametrize(
    "previous_row, current_row, next_row, expected", [("", "", "", []),
                                                      ("", "!1", "", ["1"]),
                                                      ("", "1!", "", ["1"]),
                                                      ("", "!1..2*", "", ["1", "2"]),
                                                      ("", "!123..", "", ["123"]),
                                                      ("", "!123..56$", "", ["123", "56"]),
                                                      ("", "123..", "", []),
                                                      ("$....", "123..", "", ["123"]),
                                                      ("", "123..", "...*.", ["123"]),
                                                      ("", "123..", "....&", []),
                                                      ("", "...123", "!....", [])]
)
def test_get_part_numbers(previous_row, current_row, next_row, expected):
    assert get_part_numbers(previous_row, current_row, next_row, 1) == expected


def test_sum_part_numbers():
    test_rows = ["467..114..",
                 "...*......",
                 "..35..633.",
                 "......#...",
                 "617*......",
                 ".....+.58.",
                 "..592.....",
                 "......755.",
                 "...$.*....",
                 ".664.598.."]

    assert sum_part_numbers(test_rows)[0] == 4361
    assert sum_part_numbers(test_rows)[1] == 467835

def test_sum_part_numbers_592():
    test_rows = [".....+.58.",
                 "..592.....",
                 "......755."]

    assert sum_part_numbers(test_rows)[0] == 592