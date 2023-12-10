import pytest
from solution import can_move_to_pipe, next_pipe, find_start_pipe


@pytest.mark.parametrize(
    "pipe, location, expected", [("|", (0, -1), True),
                                 ("|", (0, 1), True),
                                 ("|", (-1, 0), False),
                                 ("|", (1, 0), False),
                                 ("|", (1, 1), False),
                                 ("|", (1, -1), False),
                                 ("|", (-1, -1), False),
                                 ("|", (-1, 1), False),
                                 ("-", (0, -1), False),
                                 ("-", (0, 1), False),
                                 ("-", (-1, 0), True),
                                 ("-", (1, 0), True),
                                 ("-", (1, 1), False),
                                 ("-", (1, -1), False),
                                 ("-", (-1, -1), False),
                                 ("-", (-1, 1), False),
                                 ("L", (0, -1), False),
                                 ("L", (0, 1), True),
                                 ("L", (-1, 0), True),
                                 ("L", (1, 0), False),
                                 ("L", (1, 1), False),
                                 ("L", (1, -1), False),
                                 ("L", (-1, -1), False),
                                 ("L", (-1, 1), False),
                                 ("J", (0, -1), False),
                                 ("J", (0, 1), True),
                                 ("J", (-1, 0), False),
                                 ("J", (1, 0), True),
                                 ("J", (1, 1), False),
                                 ("J", (1, -1), False),
                                 ("J", (-1, -1), False),
                                 ("J", (-1, 1), False),
                                 ("7", (0, -1), True),
                                 ("7", (0, 1), False),
                                 ("7", (-1, 0), False),
                                 ("7", (1, 0), True),
                                 ("7", (1, 1), False),
                                 ("7", (1, -1), False),
                                 ("7", (-1, -1), False),
                                 ("7", (-1, 1), False),
                                 ("F", (0, -1), True),
                                 ("F", (0, 1), False),
                                 ("F", (-1, 0), True),
                                 ("F", (1, 0), False),
                                 ("F", (1, 1), False),
                                 ("F", (1, -1), False),
                                 ("F", (-1, -1), False),
                                 ("F", (-1, 1), False),
                                 (".", (0, -1), False),
                                 (".", (0, 1), False),
                                 (".", (-1, 0), False),
                                 (".", (1, 0), False),
                                 (".", (1, 1), False),
                                 (".", (1, -1), False),
                                 (".", (-1, -1), False),
                                 (".", (-1, 1), False),
                                 ("S", (0, -1), True),
                                 ("S", (0, 1), True),
                                 ("S", (-1, 0), True),
                                 ("S", (1, 0), True),
                                 ("S", (1, 1), True),
                                 ("S", (1, -1), True),
                                 ("S", (-1, -1), True),
                                 ("S", (-1, 1), True)]
)
def test_can_move_to_pipe(pipe, location, expected):
    assert can_move_to_pipe(pipe, location) == expected


@pytest.mark.parametrize(
     "pipe, entry, expected", [("|", (0, -1), (0, 1)),
                               ("|", (0, 1), (0, -1)),
                               ("-", (-1, 0), (1, 0)),
                               ("-", (1, 0), (-1, 0)),
                               ("L", (0, -1), (1, 0)),
                               ("L", (1, 0), (0, -1)),
                               ("J", (0, -1), (-1, 0)),
                               ("J", (-1, 0), (0, -1)),
                               ("7", (-1, 0), (0, 1)),
                               ("7", (0, 1), (-1, 0)),
                               ("F", (1, 0), (0, 1)),
                               ("F", (0, 1), (1, 0))]
)
def test_next_pipe(pipe, entry, expected):
    assert next_pipe(pipe, entry) == expected


def test_find_start_pipr():
    rows = ["-L|F7",
            "7S-7|",
            "L|7||",
            "-L-J|",
            "L|-JF"]

    assert find_start_pipe(rows) == (1, 1)