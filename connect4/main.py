# help me build the connect4 game for the terminal using python

# import the necessary modules
import numpy as np
import pygame
import sys
import math

# define the global variables
ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# define the functions
def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    # check if the top row is empty
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    # check each row in the column to see if it is empty
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    # print the board in reverse order
    print(np.flip(board, 0))

def winning_move(board, piece):
    # check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and \
            board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and \
            board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and \
            board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and \
            board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def draw_board(board):
    # draw the board
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # draw the blue rectangle
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + \
            SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # draw the black circle
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + \
            SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + \
            SQUARESIZE / 2)), RADIUS)

    # draw the red or yellow circles
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                # draw the red circle
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + \
                SQUARESIZE / 2), height - int(r * SQUARESIZE + \
                SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                # draw the yellow circle
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + \
                SQUARESIZE / 2), height - int(r * SQUARESIZE + \
                SQUARESIZE / 2)), RADIUS)
    pygame.display.update()

# initialize the board
board = create_board()
print_board(board)
game_over = False
turn = 0

# initialize pygame
pygame.init()

# define the screen size
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE / 2 - 5)

# create the screen
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

# create the font
myfont = pygame.font.SysFont("monospace", 75)

# main game loop
while not game_over:
    # ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 Make Your Selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            # check if player 1 won
            if winning_move(board, 1):
                label = myfont.render("Player 1 Wins!", 1, RED)
                screen.blit(label, (40, 10))
                game_over = True

    # ask for player 2 input
    else:
        col = int(input("Player 2 Make Your Selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            # check if player 2 won
            if winning_move(board, 2):
                label = myfont.render("Player 2 Wins!", 1, YELLOW)
                screen.blit(label, (40, 10))
                game_over = True

    # print the board
    print_board(board)
    draw_board(board)

    # switch the turn
    turn += 1
    turn %= 2

    # check if the game is over
    if game_over:
        pygame.time.wait(3000)

    # check if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
