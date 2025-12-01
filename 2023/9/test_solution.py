import pytest
from solution import get_extrapolated_value

@pytest.mark.parametrize(
    "input, expected", [([0, 0, 0, 0, 0], 0),
                        ([3, 3, 3, 3, 3], 3),
                        ([0, 3, 6, 9, 12, 15], 18)]
)
def test_get_extrapolated_value(input, expected):
    assert get_extrapolated_value(input) == expected
