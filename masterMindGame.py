import random

def generate_random_number():
    # Function to generate a random 4-digit number
    return random.randint(1000, 9999)

def count_matching_digits(guess, target):
    # Function to count the number of matching digits between two numbers
    return sum(1 for g, t in zip(guess, target) if g == t)

def provide_hint(guess, target):
    # Function to provide a hint about whether the target number is higher or lower than the guess
    if guess < target:
        print("Hint: The target number is higher.")
    elif guess > target:
        print("Hint: The target number is lower.")
    else:
        print("Hint: You guessed the number correctly!")

def play_mastermind():
    num_attempts = 100  # Maximum number of attempts allowed
    target_number = generate_random_number()  # Generate the target number

    print("Welcome to Mastermind!")
    print("Guess the 4-digit number.")
    print(f"You have {num_attempts} attempts.")

    for attempt in range(1, num_attempts + 1):
        guess = input("Enter your guess: ")

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue

        guess = int(guess)
        if guess == target_number:
            print(f"Congratulations! You guessed the number in {attempt} attempts!")
            break
        else:
            matching_digits = count_matching_digits(str(guess), str(target_number))
            print(f"Not quite the number. But you did get {matching_digits} digit(s) correct!")
            print("Also these numbers in your input were correct.")
            print(" ".join(g if g == t else 'x' for g, t in zip(str(guess), str(target_number))))
            provide_hint(guess, target_number)
            print("\n")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was: {target_number}")

if __name__ == "__main__":
    play_mastermind()
