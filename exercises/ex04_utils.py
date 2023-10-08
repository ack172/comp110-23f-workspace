"""Exercise 04- Working with Lists."""

__author__ = "730385079"


def all(list_of_numbers: list[int], number: int) -> bool:
    """Function to test if number is matched in a numerical list.""" 
    if len(list_of_numbers) == 0:
        return False  
    
    idx = 0
    while idx < len(list_of_numbers):
        if list_of_numbers[idx] != number:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    """Function designed to return the maximum value of a list.""" 
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    idx = 1
    maximum = input[0]
    while idx < len(input):
        if maximum < input[idx]:
            maximum = input[idx]
        idx += 1
    return maximum 


def is_equal(list_of_numbers1: list[int], list_of_numbers2: list[int]) -> bool:
    """Function to test if the components of two lists are completely equal.""" 
    if len(list_of_numbers1) != len(list_of_numbers2):
        return False  

    idx = 0
    while idx < len(list_of_numbers1):
        if list_of_numbers1[idx] != list_of_numbers2[idx]:
            return False
        idx += 1
    return True