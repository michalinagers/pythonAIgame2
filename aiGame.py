import random
import time

def display(board):
    print("\nCurrent board")
    for row in board:
        print("|".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def rule_based_agent(board):
    empty_cells = get_available_moves(board)

    # 1. Win if possible
    for row, col in empty_cells:
        board[row][col] = "O"
        if check_winner(board, "O"):
            board[row][col] = " "  # Undo the move
            return row, col
        board[row][col] = " "  # Undo the move

    # 2. Block opponent's move
    for row, col in empty_cells:
        board[row][col] = "X"
        if check_winner(board, "X"):
            board[row][col] = " "  # Undo the move
            return row, col
        board[row][col] = " "  # Undo the move

    # 3. Take corners
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    for row, col in corners:
        if (row, col) in empty_cells:
            return row, col

    # 4. Take center if possible
    if (1, 1) in empty_cells:
        return 1, 1

    # 5. Take any empty cell (fallback)
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe! You are 'X' and the Rule-Based Agent is 'O'.")
    display(board)

    while True:
        # Player move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, separated by space, e.g., '0 1'): ").split())
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column numbers between 0 and 2.")

        display(board)

        # Check if player wins
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

        # Rule-Based Agent move
        row, col = rule_based_agent(board)
        board[row][col] = "O"
        print(f"Rule-Based Agent placed 'O' at ({row}, {col}).")
        display(board)

        # Check if the agent wins
        if check_winner(board, "O"):
            print("Rule-Based Agent wins! Better luck next time.")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

        time.sleep(1)  # Add a 1-second pause between moves for better timing

# Run the game
play_game()
