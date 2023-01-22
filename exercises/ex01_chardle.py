"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730610489"

five_word: str = input("Enter a 5 character word: ")

if len(five_word) != 5:
    print("Error: Word must contain 5 charcaters")
    exit()

single_chtr: str = input("Enter a single character: ")
nmbr_match: int = 0

print("Searching for " + single_chtr + " in " + five_word)
if five_word[0] == single_chtr:
    print (single_chtr + " found at " + "index 1")
    nmbr_match = nmbr_match + 1

if five_word[1] == single_chtr:
    print (single_chtr + " found at " + "index 2")
    nmbr_match = nmbr_match + 1

if five_word[2] == single_chtr:
    print (single_chtr + " found at " + "index 3")
    nmbr_match = nmbr_match + 1

if five_word[3] == single_chtr:
    print (single_chtr + " found at " + "index 4")
    nmbr_match = nmbr_match + 1

if five_word[4] == single_chtr:
    print (single_chtr + " found at " + "index 5")
    nmbr_match = nmbr_match + 1

if nmbr_match > 1:
    print(str(nmbr_match) + " instances of " + single_chtr + " found in " + five_word)
if nmbr_match == 1:
    print("1" + " instance of " + single_chtr + " found in " + five_word)
if nmbr_match == 0:
    print("no" + " instances of " + single_chtr + " found in " + five_word)
