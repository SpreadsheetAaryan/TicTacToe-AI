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

    num_x = 0
    num_o = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                num_x += 1
            if board[row][col] == O:
                num_o += 1

    if num_x > num_o:
        return O
    else:
        return X
            

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception('Not valid move')

    i, j = action
    new_board = copy.deepcopy(board)

    new_board[i][j] = player(board)

    return new_board

def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def checkDig1(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == j and board[i][j] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def checkDig2(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if (len(board) - i - 1) == j and board[i][j] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    if checkRow(board, X) or checkCol(board, X) or checkDig1(board, X) or checkDig2(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or checkDig1(board, O) or checkDig2(board, O):
        return O
    else:
        return None
    
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] is EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([minval(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([maxval(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]

def minval(board):
    """
    - If terminal(s), return utility(state). If the game ended, then calculate the value to see who won.
    - Else, we set variable v to inifinity. V represents the value of the game.
    - For action in actions(s), v = Min(v, max-value(result(state, action)))
    - return v
    """

    if terminal(board):
        return utility(board)
    else:
        v = 9999999999999999999
        for action in actions(board):
            v = min(v, maxval(result(board, action)))

        return v

def maxval(board):
    """
    - If terminal(s), return utility(state). If the game ended, then calculate the value to see who won.
    - Else, we set variable v to negative inifinity. V represents the value of the game.
    - For action in actions(s), v = Max(v, min-value(result(state, action)))
    - return v
    """

    if terminal(board):
        return utility(board)
    else:
        v = -9999999999999999999
        for action in actions(board):
            v = max(v, minval(result(board, action)))

        return v