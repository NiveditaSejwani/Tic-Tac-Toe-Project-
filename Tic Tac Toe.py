# Create the game board as a list with 9 empty spaces
board = [' ' for _ in range(9)]

def print_board():
    """
    Displays the current state of the board in a 3x3 grid.
    """
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('--+---+--')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('--+---+--')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

def check_win(player):
    """
    Checks if the given player has met any win conditions.
    Returns True if the player wins, otherwise False.
    """
    return ((board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player))

def check_draw():
    """
    Determines if the game is a draw (i.e., no empty spaces left).
    Returns True if the board is full and no win condition is met.
    """
    return ' ' not in board

def player_move(player):
    """
    Prompts the player to enter a move, validates the move,
    and updates the board if the move is valid.
    """
    while True:
        try:
            # Prompt for a move and adjust for 0-indexed list
            move = int(input("Player " + player + ", enter move (1-9): ")) - 1
            # Check move is within range and the space is empty
            if move >= 0 and move < 9 and board[move] == ' ':
                board[move] = player
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    """
    Main function to execute the game loop.
    Alternates turns between players, checks for a win or draw,
    and prints the board accordingly.
    """
    current = 'X'
    while True:
        print_board()
        player_move(current)
        if check_win(current):
            print_board()
            print("Player " + current + " wins!")
            break
        if check_draw():
            print_board()
            print("It's a draw!")
            break
        # Switch player
        current = 'O' if current == 'X' else 'X'

if __name__ == "__main__":
    main()
