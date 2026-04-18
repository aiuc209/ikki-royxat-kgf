import pytest

def calculate_perimeter(lengths, widths):
    return [2 * (l + w) for l, w in zip(lengths, widths)]

@pytest.mark.parametrize("lengths, widths, expected", [
    ([1, 2, 3], [4, 5, 6], [10, 14, 18]),
    ([10, 20, 30], [40, 50, 60], [100, 140, 180]),
    ([5, 5, 5], [5, 5, 5], [20, 20, 20]),
])
def test_calculate_perimeter(lengths, widths, expected):
    assert calculate_perimeter(lengths, widths) == expected

def test_calculate_perimeter_empty_lists():
    assert calculate_perimeter([], []) == []

def test_calculate_perimeter_lists_of_different_lengths():
    with pytest.raises(ValueError):
        calculate_perimeter([1, 2, 3], [4, 5])
