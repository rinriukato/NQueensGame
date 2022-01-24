# sneakyQueens with GUI
from tkinter.tix import WINDOW
from turtle import window_height
from tkinter import messagebox
import pygame

# Intialize pygame
pygame.init()

# Constants
BLACK = (0, 0, 0)
WHITE = (250, 255, 255)
GREY = (192, 192, 192)
METAL_GREY = (142, 142, 142)
RED = (255, 0, 0)
WINDOW_WIDTH = 405
WINDOW_HEIGHT = 455
BLOCK_WIDTH = 45
BLOCK_HEIGHT = 45
BLOCK_MARGIN = 5
NUM_ROWS = 8
NUM_COLS = 8

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Queens Attack")

board = [[0 for x in range(NUM_ROWS)] for y in range(NUM_COLS)] # empty 8x8 board

# --- Button Class
class button():
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('couriernew', 25)
            text = font.render(self.text, 1, WHITE)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

def drawGrid():
    screen.fill(GREY)

    for row in range(NUM_ROWS):
        for column in range(NUM_COLS):
            if board[row][column] == 1: # Updates Grid with new Queens clicked
                color = BLACK
            elif board[row][column] == 2:
                color = RED
            else: # On start, fill with blocks
                color = WHITE
            pygame.draw.rect(screen, color, [BLOCK_MARGIN + (BLOCK_MARGIN + BLOCK_WIDTH) * column, BLOCK_MARGIN + (BLOCK_MARGIN + BLOCK_HEIGHT) * row, BLOCK_WIDTH, BLOCK_HEIGHT])

def resetBoard(board):
    for row in range(NUM_ROWS):
        for column in range(NUM_COLS):
            board[row][column] = 0

def queensSafe(board):
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if board[i][j] == 1:
                if (not checkForAttack(board,i,j)):
                    return False
    return True

def checkForAttack(board, x, y):
    # --- Check horizontal attacks
    for i in range(NUM_COLS):
        if i != y and board[x][i] == 1:
            markError(board, x, i, 'h')
            return False
    
    # --- Check for vertical attacks
    for i in range(NUM_ROWS):
        if i != x and board[i][y] == 1:
            markError(board, i, y, 'v')
            return False
    
    # --- Check for diagonal attacks
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            # not the current queens and not diagonal

            if i == x or j == y:
                continue

            slope = getSlope(i,j,x,y)

            if (abs(slope) != 1):
                continue
            # On the diagonal
            else:
                if board[i][j] == 1:
                    markError(board, i, j, 'd')
                    return False
    
    return True

def getSlope(x1,y1,x2,y2):
    return ((y2-y1)/(x2-x1))

def markError(board, x, y, direction):
    if (direction == 'h'):
        for i in range(y-1, 0, -1):
            if board[x][i] == 1:
                return
            board[x][i] = 2
            
    elif (direction == 'v'):
        for i in range(x-1, 0, -1):
            if board[i][y] == 1:
                return
            board[i][y] = 2

    else:
        for i in range(x-1, 0, -1):
            for j in range(y, 0, -1):
                if (abs(getSlope(i,j,x,y)) == 1):
                    if (board[i][j] == 1):
                        return
                    board[i][j] == 2



checkButton = button(METAL_GREY, (WINDOW_WIDTH/2) - 100, WINDOW_HEIGHT - 50, 80, 50, "Check")
resetButton = button(METAL_GREY, (WINDOW_WIDTH/2) + 20, WINDOW_HEIGHT - 50, 80, 50, "Reset")
# Keep window open
def main():
    numQueens = 0
    running = True

    while running:

        # --- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # user closed application
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                column = pos[0] // (BLOCK_WIDTH + BLOCK_MARGIN) # Normalize to grid
                row = pos[1] // (BLOCK_HEIGHT + BLOCK_MARGIN)

                if (column < NUM_COLS and row < NUM_ROWS): # Check if where user clicked is out of bounds
                    print("Click ", pos, "Grid coordinates: ", row, column)
                    if (board[row][column] == 1):
                        board[row][column] = 0
                        numQueens -= 1
                    else:
                        board[row][column] = 1
                        numQueens += 1
                
                elif checkButton.isOver(pos):
                    if (queensSafe(board)):
                        if (numQueens == 8):
                            messagebox.showinfo('Safe!','All 8 queens on the board cannot attack each other!')
                        else:
                            messagebox.showinfo('Not so fast!', 'There are {} queens right now. You need 8 to beat the game'.format(numQueens))
                    # In the GUI, make it so it shows what queen attacks who
                    else:
                        messagebox.showinfo('Uh oh', 'A queen is being attacked!')

                elif resetButton.isOver(pos):
                    resetBoard(board)
                    numQueens = 0
        
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        drawGrid()
        checkButton.draw(screen)
        resetButton.draw(screen)

        # Update Screen
        pygame.display.flip()
        pygame.display.update()

main()
pygame.quit()