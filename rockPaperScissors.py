import random

def display_scores(scores):
    print("Scoreboard: ")
    for player, score in scores.items():
        print(f"{player} : {score} wins")
    print()

def save_scores(scores):
    with open("score.txt", "w") as file:
        for player, score in scores.items():
            file.write(f"{player}:{score}\n")
            
def load_scores():
    scores = {}
    try:
        with open("scores.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                player, score = line.strip().split(":")
                scores[player] = int(score)
    except FileNotFoundError:
        pass
    return scores

def main():
    scores = load_scores()
    display_scores(scores)   

    # Introduction and rules of the game
    print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
        + "Rock vs Paper -> Paper wins \n"
        + "Rock vs Scissors -> Rock wins \n"
        + "Paper vs Scissors -> Scissor wins \n")

    while True: 
        # get users choice as input 
        print("Enter your choice: Rock, Paper, Scissors \n")
        user_choice = input("Enter your choice: ").lower()
        
        # validate user's choice input 
        while user_choice not in ['rock', 'paper', 'scissors']:
            user_choice = input("Enter a valid choice (Rock, Paper or Scissors): ").lower()
            
        # display users choice
        print(f"Users choice is: {user_choice.capitalize()}")
        
        # generate computers choice randomly
        comp_choice = random.choice(["rock", "paper", "scissors"])
        
        # ensure computer's choice is not the same as user's choice 
        while comp_choice == user_choice:
            comp_choice = random.choice(["rock", "paper", "scissors"])
            
        # display computers choice 
        print(f"Computer choice is: {comp_choice.capitalize()}")
        print(user_choice.capitalize(), "Vs", comp_choice.capitalize())
        
        result = None
        # Determine the result of the game 
        if user_choice == comp_choice:
            print("It is a DRAW")
            result = "DRAW"
        elif (user_choice == "rock" and comp_choice == "paper") or (user_choice == "paper" and comp_choice == "scissors") or (user_choice == "scissors" and comp_choice == "rock"):
            print(comp_choice.capitalize(), "wins")
            result = comp_choice.capitalize()
        else:
            print(user_choice.capitalize(), "wins")
            result = user_choice.capitalize()
        
        if result != "DRAW":
            scores[result] = scores.get(result, 0) + 1
            save_scores(scores)

        display_scores(scores)    
        
        
        # # display the outcome of the game
        # if result == "DRAW":
        #     print("It's a Tie")
        # elif result == user_choice.capitalize():
        #     print("User Wins")
        # else:
        #     print("Computer Wins")
            
        # # ask they user if they want to play again 
        # ans = input("Do you want to play again? (y/n)").lower()
        # if ans != "y":
        #     break
        # print("Thanks for playing ")
    
if __name__ == "__main__":
    main()
    