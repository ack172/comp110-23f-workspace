"""EX07- 'Dict" Unit Tests."""

__author__ = "730385079"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance


import pytest


def test_keyerror_invert() -> None:
    """Testing to see if there are multiples of the same key, use case."""
    dict1: dict[str, str] = {}
    dict1 = {"a": "b", "c": "b"}
    with pytest.raises(KeyError):
        invert(dict1)


def test_normal_usage_1_invert() -> None:
    """Testing normal usage of function given a 2 key dictionary, use case."""
    dict1: dict[str, str] = {}
    dict1 = {"a": "b", "c": "d"}
    dict2: dict[str, str] = invert(dict1)
    assert len(dict2) == 2
    for key in dict1:
        assert dict2[dict1[key]] == key


def test_normal_usage_2_invert() -> None:
    """Testing an empty dictionary to see if empty dictionary returned, edge case."""
    dict1: dict[str, str] = {}
    dict2: dict[str, str] = invert(dict1)
    assert len(dict2) == 0


def test_normal_usage_favorite_color() -> None:
    """Testing to see if that functionr eturns most used color string, use case."""
    dict1: dict[str, str] = {}
    dict1 = {"a": "blue", "c": "blue", "d": "red"}
    assert favorite_color(dict1) == "blue"


def test_normal_usage_2_favorite_color() -> None:
    """Testing to make sure that the function returns first in dictionary, use case."""
    dict1: dict[str, str] = {}
    dict1 = {"a": "blue", "c": "blue", "d": "red", "e": "red"}
    assert favorite_color(dict1) == "blue"


def test_edgecase_favorite_color() -> None:
    """Testing to make sure that the function returns first in dictionary, edge case."""
    dict1: dict[str, str] = {}
    assert len(favorite_color(dict1)) == 0


def test_normal_usage_count() -> None:
    """Testing normal usage of the count function with a 2 item list, use case."""
    list1: list[str] = ["free", "energy"]
    output: dict[str, int] = count(list1)
    for key in output:
        assert output[key] == 1

    
def test_normal_usage_2_count() -> None:
    """Testing normal usage of the count function with repeating elements, use case."""
    list1: list[str] = ["free", "energy", "free", "energy"]
    output: dict[str, int] = count(list1)
    for key in output:
        assert output[key] == 2


def test_edgecase_count() -> None:
    """Testing to make sure empty dictionary is returned when encounters an empty list, edge case."""
    list1: list[str] = []
    output: dict[str, int] = count(list1)
    assert len(output) == 0


def test_normal_usage_alphabetizer() -> None:
    """Testing normal usage of the alpahbetizer function given two similar started words, use case."""
    list1: list[str] = ["count", "character", "dog"]
    output: dict[str, list[str]] = alphabetizer(list1)
    assert len(output) == 2
    for key in output:
        for word in output[key]:
            assert key == word[0].lower()


def test_normal_usage_alphabetizer_2() -> None:
    """Testing normal usage of the alphabetizer function given three different started words, use case."""
    list1: list[str] = ["count", "elephant", "dog"]
    output: dict[str, list[str]] = alphabetizer(list1)
    assert len(output) == 3
    for key in output:
        for word in output[key]:
            assert key == word[0].lower()


def test_edgecase_alphabetizer() -> None:
    """Testing to make sure empty dictionary is returned when encounters an empty list, edge case."""
    list1: list[str] = []
    output: dict[str, list[str]] = alphabetizer(list1)
    assert len(output) == 0


def test_normal_usage_updateattendance() -> None:
    """Testing normal usage of the update attendance function given a new day of the week, use case."""
    dict1: dict[str, list[str]] = {"Monday": ["Bob", "Jeane"]}
    str1: str = "Tuesday"
    str2: str = "Joe"
    assert len(update_attendance(dict1, str1, str2)) == 2
    assert len(dict1["Monday"]) == 2
    assert len(dict1["Tuesday"]) == 1


def test_normal_usage_updateattendance_2() -> None:
    """Testing normal usage of the update attendance function given the same day of the week, use case."""
    dict1: dict[str, list[str]] = {"Monday": ["Bob", "Jeane"]}
    str1: str = "Monday"
    str2: str = "Joe"
    assert len(update_attendance(dict1, str1, str2)) == 1
    assert len(dict1["Monday"]) == 3


def test_edgecase_updateattendance() -> None:
    """Testing to make sure empty dictionary is returned when encounters an empty list, edge case."""
    dict1: dict[str, list[str]] = {"Monday": ["Bob", "Jeane"]}
    str1: str = ""
    str2: str = ""
    assert len(update_attendance(dict1, str1, str2)) == 1
    assert len(dict1["Monday"]) == 2
