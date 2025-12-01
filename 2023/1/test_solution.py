import pytest
from solution import calculate, calculate_line, is_start_of_number_word

@pytest.mark.parametrize(
    "input, expected", [("oneas", 1),
                        ("twoas", 2),
                        ("threeas", 3),
                        ("fouras", 4),
                        ("fiveas", 5),
                        ("sixas", 6),
                        ("sevenas", 7),
                        ("eightas", 8),
                        ("nineas", 9),
                        ("notas", False)]
)
def test_is_start_of_number_word(input, expected):
    assert is_start_of_number_word(input) == expected

@pytest.mark.parametrize(
    "test_input,expected", [("1abc2", 12),
                            ("pqr3stu8vwx", 38),
                            ("a1b2c3d4e5f", 15),
                            ("treb7uchet", 77)]
)
def test_calculate_line(test_input, expected):
    assert calculate_line(test_input) == expected


@pytest.mark.parametrize(
    "input, expected", [("two1nine", 29),
                        ("eightwothree", 83),
                        ("abcone2threexyz", 13),
                        ("xtwone3four", 24),
                        ("4nineeightseven2", 42),
                        ("zoneight234", 14),
                        ("7pqrstsixteen", 76)]
)
def test_calculate_line_contains_number_word(input, expected):
    assert calculate_line(input) == expected


def test_calculate():
    lines = ["1abc2",
             "pqr3stu8vwx",
             "a1b2c3d4e5f",
             "treb7uchet"]

    assert calculate(lines) == 142