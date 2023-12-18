def minimax(board, maximizing_player):
    if check_winner(board) == 1:
        return -1
    elif check_winner(board) == 2:
        return 1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    eval = minimax(board, False)
                    board[i][j] = 0
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    eval = minimax(board, True)
                    board[i][j] = 0
                    min_eval = min(min_eval, eval)
        return min_eval


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if  board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0 or board[0][2] == board[1][1] == board[2][0] != 0:
        return board[1][1]

    return 0


def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def get_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 2
                move_val = minimax(board, False)
                board[i][j] = 0

                if move_val > best_val:
                    best_move = (j, i)
                    best_val = move_val

    return best_move
