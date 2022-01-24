# N-Queens Problem + GUI?
# E = Empty, Q = Queen. 8x8 standard chessboard
# Checks if the current board has any queens attacking each other


## Main Stuff
cols = 8
rows = 8
curBoard = [
                ['Q','E','E','E','E','E','E','E'],
                ['E','E','Q','E','E','E','E','E'],
                ['E','E','E','E','E','E','E','E'],
                ['E','E','E','E','E','E','E','E'],
                ['E','Q','E','E','E','E','E','E'],
                ['E','E','E','E','E','E','E','E'],
                ['E','E','E','E','E','E','E','E'],
                ['E','E','E','Q','E','E','E','E']
             ]

def queensSafe(board):
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'Q':
                if (not checkForAttack(board,i,j)):
                    return False
    return True

def checkForAttack(board, x, y):
    ## Check horizontal attacks
    for i in range(cols):
        if i != y and board[x][i] == 'Q':
            print('Queen[{},{}] is attacked horizontally by Queen[{},{}]'.format(x,y,x,i))
            return False
    
    ## Check for vertical attacks
    for i in range(rows):
        if i != x and board[i][y] == 'Q':
            print('Queen[{},{}] is attacked vertically by Queen[{},{}]'.format(x,y,i,y))
            return False
    
    ## Check for diagonal attacks
    for i in range(rows):
        for j in range(cols):
            # not the current queens and not diagonal
            if (i == x or j == y) or (getSlope(i,j,x,y) != 1):
                continue
            # On the diagonal
            else:
                if board[i][j] == 'Q':
                    print('Queen[{},{}] is attacked diagonallyby Queen[{},{}]'.format(x,y,i,j))
                    return False
    
    return True

def getSlope(x1,y1,x2,y2):
    return abs((y2-y1)/(x2-x1))


if (queensSafe(curBoard)):
    print('All queens positions are safe!')
# In the GUI, make it so it shows what queen attacks who
else:
    print('A queen is being attacked!')