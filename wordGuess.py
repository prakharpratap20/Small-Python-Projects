import random

# library that we use in order to choose
# on random words from a list of words

name = input("What is your name? : ")  # getting input from the user

print(f"Good Luck ! {name}")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# this function will choose one random word form this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ""

turns = 12  # any number of turns can be used here

while turns > 0:
    failed = 0  # count the number of times a user fails
    for char in word:  # all characters from the input word
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1  # for every failure 1 will be incremented in failure

    if failed == 0:  # user will win the game if failure is 0
        print("\nYou Win")  # this will be the output
        print(f"The word is {word}")  # this prints the correct word
        break

    print()
    guess = input("Guess a character: ")

    guesses += guess  # storing every input character in guesses

    # check input with the character in the word
    if guess not in word:
        turns -= 1
        # if the character doesn't match the word then "Wrong" will be given
        print("Wrong")
        print(f"You have {turns} more guesses")

        if turns == 0:
            print("You Lose")
