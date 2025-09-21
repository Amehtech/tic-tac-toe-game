# tic-tac-toe-game
this is a computer vs human game 
import random
board = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", ""]

current_player = "X"
winner = None
game_running = True



#printing the game board
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

print_board(board)


#take the player input
def player_input(player):
    inp = int(input("Enter a number 1-9!"))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = current_player
    else:
        print("OOPS player is already in that spot!")

#check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#function to check row
def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonals(board):
    global winner
    if board[0] == board[4] == board[9] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

#function to check if there is a tie
def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print(" Its a Tie!")
        game_running = False

# function for computer moves
def computer(board):
    while current_player == "0":
        position = random.randint(0,8)
        if board[position] == "-":
           board[position] = "0"
           switch_player()

#creating a master function
def check_for_win():
    if check_diagonals(board) or check_horizontal(board) or check_row(board):
        print(f"the winner is {winner}")

#switch the player
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    else:
        current_player = "X"
#check for win or tie again
while game_running:
    print_board(board)
    player_input(board)
    check_for_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_for_win()
    check_tie(board)



