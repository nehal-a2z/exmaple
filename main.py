import colorama

colorama.init(autoreset=True)

def print_board(board):
    for row in board:
        colored_row = [colorama.Fore.CYAN + cell + colorama.Fore.RESET if cell != " " else cell for cell in row]
        print(" | ".join(colored_row))
        print(colorama.Fore.YELLOW + "-" * 9 + colorama.Fore.RESET)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers.")

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == "y":
        play_tic_tac_toe()

if __name__ == "__main__":
    print(colorama.Fore.GREEN + "Welcome to Tic-Tac-Toe!" + colorama.Fore.RESET)
    play_tic_tac_toe()
