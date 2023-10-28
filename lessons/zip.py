"""Combining two lists into a dictionary."""

__author__ = "730385079"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Function to combine two lists into a dictionary with str keys and int values."""
    if len(list1) != len(list2) or len(list1) == 0:
        return dict()
    new_dict: dict[str, int] = {}
    for elem in range(len(list1)):
        new_dict[list1[elem]] = list2[elem]
    return new_dict