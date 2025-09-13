

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print(" | ".join(row))
        if row != board[6:]:
            print("--+---+--")


def check_win(board, player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)


def is_draw(board):
    return all(cell != ' ' for cell in board)


def get_available_moves(board):
    return [i for i in range(9) if board[i] == ' ']


def minimax(board, depth, alpha, beta, is_maximizing, ai_player, human_player):
    if check_win(board, ai_player):
        return 10 - depth
    if check_win(board, human_player):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move] = ai_player
            eval = minimax(board, depth + 1, alpha, beta, False, ai_player, human_player)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move] = human_player
            eval = minimax(board, depth + 1, alpha, beta, True, ai_player, human_player)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def find_best_move(board, ai_player, human_player):
    best_score = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move] = ai_player
        score = minimax(board, 0, float('-inf'), float('inf'), False, ai_player, human_player)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


def play_game():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe with AI (Alpha-Beta Pruning)\n")
    player_choice = input("Choose your symbol (X/O): ").upper()

    while player_choice not in ['X', 'O']:
        player_choice = input("Invalid input. Choose X or O: ").upper()

    human_player = player_choice
    ai_player = 'O' if human_player == 'X' else 'X'
    current_turn = 'X'  # X always starts

    while True:
        print("\nCurrent board:")
        print_board(board)

        if current_turn == human_player:
            try:
                move = int(input("Your move (0-8): "))
                if board[move] != ' ':
                    print("Invalid move, spot taken.")
                    continue
                board[move] = human_player
            except (ValueError, IndexError):
                print("Invalid input. Choose a number between 0-8.")
                continue
        else:
            print("AI is making a move...")
            move = find_best_move(board, ai_player, human_player)
            board[move] = ai_player

        if check_win(board, current_turn):
            print_board(board)
            print(f"\n{current_turn} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        current_turn = ai_player if current_turn == human_player else human_player


if __name__ == "__main__":
    play_game()
