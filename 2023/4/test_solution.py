import pytest
from solution import parse_row, get_matching_numbers, get_score

def test_parse_row():
    row = 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'

    result = parse_row(row)
    assert result[0] == [41, 48, 83, 86, 17]
    assert result[1] == [83, 86, 6, 31, 17, 9, 48, 53]


def test_get_matching_numbers():
    result = get_matching_numbers([41, 48, 83, 86, 17],
                                  [83, 86, 6, 31, 17, 9, 48, 53])

    assert result == [83, 86, 17, 48]

@pytest.mark.parametrize(
    "input, expected", [([83, 86, 17, 48], 8),
                        ([32, 61], 2),
                        ([84], 1),
                        ([], 0)]
)
def test_get_score(input, expected):
    assert get_score(input) == expected