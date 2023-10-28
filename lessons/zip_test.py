"""Test my zip function."""

__author__ = "730385079"

from lessons.zip import zip


def test_nonmatching_lengths_of_lists() -> None:
    """Testing to ensure lengths of lists match, edge case."""
    list1: list[int] = [2]
    list2: list[int] = [2, 3]
    assert len(zip(list1, list2)) == 0


def test_normal_usage_1() -> None:
    """Testing normal usage of function with two identical lists, use case."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [1, 2, 3]
    result_dict = zip(list1, list2)
    assert len(result_dict) == 3
    for elem in list1:
        assert result_dict[elem] == elem


def test_normal_usage_2() -> None:
    """Testing normal usage of function with two non-matching (but equal length) lists, use case."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    result_dict = zip(list1, list2)
    assert len(result_dict) == 3
    idx: int = 0
    while idx < len(list1):
        assert result_dict[list1[idx]] == list2[idx]
        idx += 1
