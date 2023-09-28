"""EX02- One shot wordle."""

__author__ = "730385079"

# establishing a secret word
secret_word: str = "python"
# asking for guess and matching to input
word: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(word) != len(secret_word): 
    word = input(f"that was not {len(secret_word)} letters! Try again: ")

if len(word) == len(secret_word): 
    # introducing named constants for emojis        
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

# defining matching index and establishing string for emojis to print into
    idx = 0
    resulting_emoji: str = ""
   
    while idx < len(secret_word):
        # introducing alternate index and boolean for yellow block (to determine if the letter is in the word at all)
        # introduced in the loop to make sure it restarts for each letter
        alt_idx = 0
        guessed_character = False
        if word[idx] == secret_word[idx]:
            resulting_emoji += GREEN_BOX
        # if the letters do not match exactly, this loop will test if the letter is in the word at all
        else:
            while alt_idx < len(secret_word):
                if word[idx] == secret_word[alt_idx]:
                    guessed_character = True
                    # boolean is true when the alt idx matches the guess index
                alt_idx += 1        
            if guessed_character is True:  
                resulting_emoji += YELLOW_BOX
            else:
                resulting_emoji += WHITE_BOX
        # increasing the index restarts the while loop
        idx += 1
    print(resulting_emoji)

# does the word equal the secret word?
    if word == secret_word:
        print("Woo! You got it!")   
    else:
        print("Not quite. Play again soon!")