import colorama
from sound_manager import SoundManagerX

class InvalidMoveError(Exception):
    """Custom exception for invalid moves."""
    pass

class GameState:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.sound_manager = SoundManagerX(self.board)

    def reset(self):
        self.__init__()

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

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

def validate_move(row: int, col: int, board) -> bool:
    """Validate if the move is within bounds and the cell is empty."""
    if not (0 <= row <= 2 and 0 <= col <= 2):
        raise InvalidMoveError("Position out of bounds. Choose numbers between 0-2.")
    if board[row][col] != " ":
        raise InvalidMoveError("That position is already taken.")
    return True

def get_player_move(board) -> tuple[int, int]:
    """Get and validate player move."""
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            validate_move(row, col, board)
            return row, col
        except ValueError:
            print("Invalid input. Please enter numbers.")
        except InvalidMoveError as e:
            print(f"Invalid move: {e}")

def play_tic_tac_toe():
    game = GameState()
    
    while True:
        print_board(game.board)
        print(f"Player {game.current_player}'s turn")
        
        row, col = get_player_move(game.board)
        game.board[row][col] = game.current_player
        game.sound_manager.play_move_sound()

        if check_winner(game.board, game.current_player):
            print_board(game.board)
            print(f"Player {game.current_player} wins!")
            break
        elif is_full(game.board):
            print_board(game.board)
            print("It's a draw!")
            break

        game.current_player = "O" if game.current_player == "X" else "X"

    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again in ['y', 'n']:
            if play_again == 'y':
                game.reset()
                play_tic_tac_toe()
            break
        print("Please enter 'y' or 'n'")

if __name__ == "__main__":
    colorama.init(autoreset=True)
    print(colorama.Fore.GREEN + "Welcome to Tic-Tac-Toe!" + colorama.Fore.RESET)
    try:
        play_tic_tac_toe()
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
