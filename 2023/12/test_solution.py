from solution import is_match, create_combinations
import pytest

@pytest.mark.parametrize(
    "input, pattern, expected", [("#......", "2", False),
                                 ("#......", "1", True),
                                 ("...#..#", "2", False),
                                 ("...#..#", "1,1", True),
                                 ("...##..", "1,1", False),
                                 ("...#.##", "2, 1", False)]
)
def test_is_match(input, pattern, expected):
    assert is_match(input, pattern) == expected


def test_create_combinations():
    input = "?###????????"
    pattern = "3,2,1"
    expected = [
        ".###.##.#...",
        ".###.##..#..",
        ".###.##...#.",
        ".###.##....#",
        ".###..##.#..",
        ".###..##..#.",
        ".###..##...#",
        ".###...##.#.",
        ".###...##..#",
        ".###....##.#"
    ]
    assert create_combinations(input, pattern) == expected
