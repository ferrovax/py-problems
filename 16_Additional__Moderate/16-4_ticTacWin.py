# 16.4
# This solution assumes straight-forward 3x3 game

def hasWon(board):
    for i in range(len(board)):
        # rows
        if checkTriple(board[i][0], board[i][1], board[i][2]):
            return board[i][0]

        # columns
        if checkTriple(board[0][i], board[1][i], board[2][i]):
            return board[0][i]

    #diagonals
    if checkTriple(board[0][0], board[1][1], board[2][2]) or checkTriple(board[0][2], board[1][1], board[2][0]):
        return board[1][1]

    return None

def checkTriple(a, b, c):
    if a == None:
        return False

    return a == b and b == c
