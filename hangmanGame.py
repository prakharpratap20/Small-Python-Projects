import random

fruits = [
    'apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple',
    'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry',
    'peach', 'lychee', 'muskmelon'
]


def choose_word():
    return random.choice(fruits)


def display_word(word, guessed_letters):
    displayed_word = [c if c in guessed_letters else '_' for c in word]
    return ' '.join(displayed_word)


def main():
    word = choose_word()
    guessed_letters = set()
    chances = len(word) + 2

    print("Guess the word! HINT: The word is the name of a fruit.")
    print(display_word(word, guessed_letters))

    try:
        while chances > 0:
            guess = input("Enter a letter to guess: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You have already guessed that letter.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("Correct!")
            else:
                chances -= 1
                print(f"Incorrect! You have {chances} chances remaining.")

            displayed_word = display_word(word, guessed_letters)
            print(displayed_word)

            if ''.join(c for c in displayed_word if c != ' ') == word:
                print(f"Congratulations! You guessed the word: {word}")
                break

        if chances == 0 and ''.join(c for c in displayed_word if c != ' ') != word:
            print(f"You lost! The word was: {word}")

    except KeyboardInterrupt:
        print("\nBye! Try Again.")


if __name__ == "__main__":
    main()
