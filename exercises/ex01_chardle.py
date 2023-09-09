"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730385079"

# establishing input variables
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
if len(word) != 5:
    exit()
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    print("Error: Character must be a single character.")
if len(letter) != 1:
    exit()
print("Searching for " + letter + " in " + word )

# checking indices for matches
if word[0] == letter:
    print(letter + " found at index 0")
if word[1] == letter:
    print(letter + " found at index 1")
if word[2] == letter:
    print(letter + " found at index 2")
if word[3] == letter:
    print(letter + " found at index 3")
if word[4] == letter:
    print(letter + " found at index 4")

# counting matching indexes
num_of_matching_indexes: int= 0
if word[0] == letter:
    num_of_matching_indexes = num_of_matching_indexes + 1
if word[1] == letter:
    num_of_matching_indexes = num_of_matching_indexes + 1 
if word[2] == letter:
    num_of_matching_indexes = num_of_matching_indexes + 1 
if word[3] == letter:
    num_of_matching_indexes = num_of_matching_indexes + 1 
if word[4] == letter:
    num_of_matching_indexes = num_of_matching_indexes + 1  
if num_of_matching_indexes == 0:
    print("No instance of " + letter + " found in " + word)  
if num_of_matching_indexes == 1:
    print(str(num_of_matching_indexes) + " instance of " + letter + " found in " + word)  
if num_of_matching_indexes > 1:
    print(str(num_of_matching_indexes) + " instances of " + letter + " found in " + word)  