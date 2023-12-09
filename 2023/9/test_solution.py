import pytest
from solution import get_extrapolated_value, get_pretrapolated_value

@pytest.mark.parametrize(
    "input, expected", [([0, 0, 0, 0, 0], 0),
                        ([3, 3, 3, 3, 3], 3),
                        ([0, 3, 6, 9, 12, 15], 18)]
)
def test_get_extrapolated_value(input, expected):
    assert get_extrapolated_value(input) == expected


@pytest.mark.parametrize(
    "input, expected", [([0, 0, 0, 0, 0], 0),
                        ([2, 2, 2], 2),
                        ([0, 2, 4, 6], -2),
                        ([3, 3, 5, 9, 15], 5),
                        ([10, 13, 16, 21, 30, 45], 5)]
)
def test_get_pretrapolated_value(input, expected):
    assert get_pretrapolated_value(input) == expected