# return the nearest multiple to 4
def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near 

def lose():
    print("\n\n YOU LOSE !")
    print("Better luck next time !")
    exit(0)
    
# checks whether the numbers are consecutive 
def check(nums):
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] != 1:
            return False
    return True

# function for player's turn 
def player_turn():
    print("\n Your Turn.")
    print("\n How many numbers do you wish to enter? (1 to 3)")
    num_input = int(input('> '))
    
    if 1 <= num_input <= 3:
        comp_turn = 4 - num_input
    else:
        print('Wrong input. You are disqualified from the game.')
        lose()
        
    inputs = []
    for i in range(num_input):
        num = int(input("Enter the number: "))
        inputs.append(num)
        
    return inputs, comp_turn

# function for computers turn
def computer_turn(last_num):
    print("Computer's Turn.")
    comp_turn = nearestMultiple(last_num) - last_num
    if comp_turn == 4:
        comp_turn = 3
        
    inputs = []
    for i in range(comp_turn):
        inputs.append(last_num + i + 1)
        
    return inputs, comp_turn

# function to start the game
def start_game():
    numbers = []
    last_number = 0
    
    while True:
        print("Enter 'F' to take the First Chance.")
        print("Enter 'S' to take the Second Chance.")
        chance = input('> ').upper()
        
        if chance == "F":
            while last_number < 21:
                player_inputs, comp_turn = player_turn()
                numbers.extend(player_inputs)
                last_number = numbers[-1]
                
                if last_number == 21:
                    lose()
                else:
                    comp_inputs, _ = computer_turn(last_number)
                    numbers.extend(comp_inputs)
                    last_number = numbers[-1]
                    print("Order of inputs after computers turn is: ")
                    print(numbers)
                    
                    if last_number == 21:
                        lose()
                        
        elif chance == "S":
            last_number = 0
            while last_number < 20:
                comp_inputs, comp_turn = computer_turn(last_number)
                numbers.extend(comp_inputs)
                last_number = numbers[-1]
                print("Order of inputs after computer's turn is:")
                print(numbers)
                
                if last_number == 20:
                    lose()
                else:
                    print("Your Turn")
                    print("How many numbers you wish to enter? (1 to 3)")
                    num_inputs = int(input('> '))
                    inputs = []
                    for i in range(num_inputs):
                        num = int(input("Enter the number: "))
                        inputs.append(num)
                        
                    numbers.extend(inputs)
                    last_number = numbers[-1] 
                    
                    if not check(numbers):
                        print("\n You did not input consecutive integers. ")
                        lose()
                        
            print("\n\n Congratulations!")
            print("You WON!")
            exit(0) 

# main function
def main():
    print("Welcome to the 21 Number Game!")
    while True:
        print("\n Do you want to play the 21 number game? (Yes/No)")
        ans = input('> ').lower()
        
        if ans == "yes":
            start_game()
        else:
            print("Do you want to quit the game? (yes/no)")
            nex = input('> ').lower()
            if nex == "yes":
                print("You are quitting the game..")
                exit(0)
            elif nex == "no":
                print("Continuing...")
            else:
                print("Wrong Choice")
                
if __name__ == "__main__":
    main()

                          
          