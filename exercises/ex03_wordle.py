"""EX03- Structured Wordle Exercise."""

__author__ = "730385079"


def contains_char(searched_string: str, search_character: str) -> bool:
    """Purpose of contains_char is to see if the guessed string contains a given character."""
    # search character is the character that is being searched for within searched string
    # asserted to be 1 to make sure its one only character
    assert len(search_character) == 1
    # establishing an index to search with
    idx = 0
    while idx < len(searched_string):
        if searched_string[idx] == search_character:
            return True
        else:
            # increase index to see if there are any matches within the word
            idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis whose color codifies the match of a single character to a word."""
    assert len(guess) == len(secret)
    # introducing named constants
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # establishing counting index
    idx = 0
    resulting_emoji: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            # if the guess and secret indexes match, print green emoji
            resulting_emoji += GREEN_BOX
        else:
            # calling earlier function (contains char) to check if the guess contains any 
            # of the same characters as the word
            if contains_char(secret, guess[idx]) is True:  
                resulting_emoji += YELLOW_BOX
            else:
                resulting_emoji += WHITE_BOX
        idx += 1
    return resulting_emoji


def input_guess(expected_length: int) -> str:
    """Function must return the user's guess of correct length to the caller."""
    word: str = input(f"Enter a {expected_length} character word: ")
    while len(word) != expected_length: 
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # establishing secret word
    secret_word: str = "codes"
    # guess number is variable to determine the number of turns the user has left
    guess_number = 1
    exit_game = False
    while not exit_game:
        print(f" === Turn {guess_number}/6 === ")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            # program exits early if the user reaches the guess word
            exit_game = True
        else:
            guess_number += 1
        if guess_number > 6:
            exit_game = True
    if guess == secret_word:
        print(f"You won in {guess_number}/6 turns! ")
    else:
        print("X/6 - Sorry, try again tomorrow!")


# allows function to be run as a module
if __name__ == "__main__":
    main()