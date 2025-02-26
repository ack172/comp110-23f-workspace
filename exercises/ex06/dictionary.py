"""EX06- Implement function skeletons and interconversions."""

__author__ = "730385079"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert a key and value for a given dictionary."""
    output: dict[str, str] = {}
    for key in input:
        for key2 in output:
            if input[key] == key2:
                raise KeyError(f"key already exists: {input[key]}")
        output[input[key]] = key
    return output


def favorite_color(names_colors: dict[str, str]) -> str:
    """Given a list of names and colors, returns color that appears most."""
    output: dict[str, int] = {}
    # initialize values to 0
    for key in names_colors:
        output[names_colors[key]] = 0
    # add when encounter multiple instances of key
    for key in names_colors:
        output[names_colors[key]] += 1
    max: int = 0
    favorite_str: str = ""
    # if output[key] is greater than max, output[key] becomes new max
    for key in output:
        if max < output[key]:
            max = output[key]
            favorite_str = key
    return favorite_str


def count(input: list[str]) -> dict[str, int]:
    """Produces a list where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    output: dict[str, int] = {}
    # for loop iterates through keys in the input
    for key in input:
        if key in output:
            output[key] += 1
        else:
            output[key] = 1 
    return output


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    output: dict[str, list[str]] = {}
    for word in input:
        key: str = word[0].lower()
        if key in output:
            output[key].append(word)
        else:
            new_list: list[str] = []
            output[key] = new_list
            output[key].append(word)
    return output


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This function will mutate and return that dictionary."""
    if len(day) == 0 or len(student) == 0:
        return input
    if day in input:
        for person in input[day]:
            if person == student:
                return input
        input[day].append(student)
    else:
        new_list: list[str] = []
        input[day] = new_list
        input[day].append(student)
    return input