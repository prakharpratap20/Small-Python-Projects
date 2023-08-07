import random

# def initialize_board(): # create an empty 4*4 board with 2 random tiles (2 or 4) at the start
#     board = [[0]*4 for _ in range(4)]
#     add_random_tile(board)
#     add_random_tile(board)
#     return board
def initialize_board():
    board = [[0]*4 for _ in range(4)]
    print("Initialized Board dimensions:", len(board), "x", len(board[0]))
    add_random_tile(board)
    add_random_tile(board)
    return board


def add_random_tile(board): # add a random tile (2 with 90% probability, 4 with 10% probability) to an empty cell on the board
    print("Board dimensions:", len(board), "x", len(board[0]))
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4
        
def print_board(board): # display the current state of board
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))
        
def slide_left(row): # helper function to slide the tiles in a row to the left and merge adjacent equal tiles
    new_row = [cell for cell in row if cell != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i + 1]:
            new_row[i] *= 2
            new_row[i + 1] = 0
    new_row = [cell for cell in new_row if cell != 0] + [0] * row.count(0)
    return new_row

def transpose(board): # helper function to transpose the board (swap rows with columns )
    return [list(row) for row in zip(*board)]

def move_left(board): # perform a move to the left in the board
    return [slide_left(row) for row in board]

def move_right(board): # perform a move to the right in the board
    reversed_board = [row[::-1] for row in board]
    new_board = move_left(reversed_board)
    return [row[::-1] for row in new_board]

def move_up(board): # perform a move upward in the board (transpose, move left and transpose back )
    transposed_board = transpose(board)
    new_board  = move_left(transposed_board)
    return transpose(new_board)

def move_down(board): # perform a move downwards in the board (transpose, move right and transpose back)
    transposed_board = transpose(board)
    new_board = move_right(transposed_board)
    return transpose(new_board)

def is_game_over(board): # check if the game is over (win condition or no valid moves left).
    for row in board:
        if 2048 in row:
            return True
        for row in transpose(board):
            if 2048 in row:
                return True
    return not any(0 in row for row in board)
    
def main(): # main game loop 
    board = initialize_board()
    print_board(board)
    
    while not is_game_over(board):
        move = input("Enter move (w/a/s/d): ").lower()
        
        if move == "w":
            board = move_up(board)
        elif move == "a":
            board = move_left(board)
        elif move == "s":
            board = move_down(board)
        elif move == "d":
            board = move_right(board)
        else:
            print("Invalid Move. Use 'w', 'a', 's' or 'd'")
            
        add_random_tile(board)
        print_board(board)
    
    print("Game Over! You reached 2048! ")
    
if __name__ == "__main__":
    main()

            
    
    
    
    
    


    
    
    
    
    