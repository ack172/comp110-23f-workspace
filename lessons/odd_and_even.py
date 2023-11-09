"""Practicing function writing with lists."""

def odd_and_even(input: list[int]) -> list[int]:
    """Returns a new list containing the elements of the input list that are odd and have an even index."""
    output_list: list[int] = {}
    idx: int = 0
    while idx < len(input):
        if input[idx] % 2 != 0 and idx % 2 == 0:
            output_list.append(input[idx])
        idx += 1
    return output_list