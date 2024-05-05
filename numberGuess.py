import random 
import math 

# Taking input 
lower = int(input("Enter Lower bound :- "));
upper = int(input("Enter Upper bound :- "));

# generating random number between the lower and upper
x = random.randint(lower, upper)
print(f"\n\t You've only {round(math.log(upper - lower + 1, 2))} chances to guess the integer! \n")

# initalizing the number of guesses
count = 0

# for calculation of minimum number of guesses depend upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    
    # taking guessing number as input
    guess = int(input("Guess a number :- "))
    
    # Condition testing
    if x == guess:
        print(f"Congratulations you did it in {count} try")
        break # once guessed loop will break 
    elif x > guess:
        print("You guessed too small!")
    else:
        print("You guessed to high!")

# if guessing is more than required guesses, 
# show this output.
if count >= math.log(upper - lower + 1, 2):
    print(f"\n The number is {x}")
    print("\t Better Luck Next Time ")
    
    
    