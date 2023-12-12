from solution import is_match, create_combinations, unfold
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

@pytest.mark.parametrize(
    "row, expected_input, expected_pattern", [(".# 1", ".#?.#?.#?.#?.#", "1,1,1,1,1"),
                                              ("???.### 1,1,3", "???.###????.###????.###????.###????.###", "1,1,3,1,1,3,1,1,3,1,1,3,1,1,3")]
)
def test_unfold(row, expected_input, expected_pattern):
    assert unfold(row) == (expected_input, expected_pattern)
