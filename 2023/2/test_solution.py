import pytest
from solution import process_line, is_game_possible

@pytest.mark.parametrize(
    "input, expected", [("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
                        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
                        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", False),
                        ("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", False),
                        ("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True)]
)
def test_pis_game_possible(input, expected):
    game = process_line(input)

    assert is_game_possible(game, 12, 13, 14) == expected