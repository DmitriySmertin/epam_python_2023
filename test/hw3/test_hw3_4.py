import pytest

from src.hw3.hw3_4 import combinations


@pytest.mark.parametrize(
    "given, expected",
    [
        (
            [[1, 2], [3, 4]],
            [
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
            ],
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [
                [1, 4, 7],
                [1, 4, 8],
                [1, 4, 9],
                [1, 5, 7],
                [1, 5, 8],
                [1, 5, 9],
                [1, 6, 7],
                [1, 6, 8],
                [1, 6, 9],
                [2, 4, 7],
                [2, 4, 8],
                [2, 4, 9],
                [2, 5, 7],
                [2, 5, 8],
                [2, 5, 9],
                [2, 6, 7],
                [2, 6, 8],
                [2, 6, 9],
                [3, 4, 7],
                [3, 4, 8],
                [3, 4, 9],
                [3, 5, 7],
                [3, 5, 8],
                [3, 5, 9],
                [3, 6, 7],
                [3, 6, 8],
                [3, 6, 9],
            ],
        ),
    ],
)
def test_combinations(given, expected):
    assert combinations(*given) == expected
