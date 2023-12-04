import pytest
from solution import parse_row, get_matching_numbers, get_score, get_total_cards, get_cards

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


def test_get_total_cards():
    rows = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

    all_matching_numbers = [get_matching_numbers(*parse_row(row)) for row in rows]
    assert get_total_cards(get_cards(all_matching_numbers)) == 30