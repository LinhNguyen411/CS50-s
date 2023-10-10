"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = 0
    O_count = 0
    for row in board:
        X_count += row.count('X')
        O_count += row.count('O')
    if X_count > O_count:
        return 'O'
    else:
        return 'X'

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] is None:
                possible.add((i,j))
    return possible



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    results = copy.deepcopy(board)
    if results[action[0]][action[1]] is not None:
        raise Exception('Invalid')
    results[action[0]][action[1]] = player(board)
    return results

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    length = len(board)
    for row in board:
        if row.count('X') == length:
            return 'X'
        elif row.count('O') == length:
            return 'O'
    for i in range(length):
        if board[0][i] == board[1][i] == board[2][i] == 'X':
            return 'X'
        elif board[0][i] == board[1][i] == board[2][i] == 'O':
            return 'O'
    if board[0][0] == board[1][1] == board[2][2] == 'X' or board[2][0] == board[1][1] == board[0][2] == 'X':
        return 'X'
    elif board[0][0] == board[1][1] == board[2][2] == 'O' or board[2][0] == board[1][1] == board[0][2] == 'O':
        return 'O'
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    return all([all(row) for row in board])


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_ = winner(board)
    if winner_ == 'O':
        return -1
    elif winner_ == 'X':
        return 1
    else:
        return 0

def Max_Value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, Min_Value(result(board,action)))
    return v
def Min_Value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, Max_Value(result(board,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # optimal = max({action : Min_Value(result(board, action)) for action in actions(board)}.items(), key= lambda x: x[1])
    if terminal(board):
        return None
    if player(board) == 'X':
        optimal = max([[action, Min_Value(result(board, action))] for action in actions(board)], key= lambda x: x[1])
    else:
        optimal = min([[action, Max_Value(result(board, action))] for action in actions(board)], key= lambda x: x[1])
    return optimal[0]
