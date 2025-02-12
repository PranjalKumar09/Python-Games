""" 
going through row means in vertically while in column means horizontally

"""


from tkinter.font import families
from turtle import screensize, width
import numpy as np 
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,0,255)
SQUARE_SIZE = 100


def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board 


def drop_piece(board , row , col , piece):
    board[row][col] = piece
    
def is_Valid_location(board , col):
    return board[ROW_COUNT-1][col] == 0
def get_next_open_row(board , col):
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row
    return -1

def print_board (board):
    print(np.flip(board , 0))
def winning_move(board , piece):
    # checking horizontals
    for col in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT):
            if board[row][col] == piece and board[row][col+1] == piece and board[row][col+2] == piece and board[row][col+3] == piece:
                return True
    # checking vertically
    for row in range(ROW_COUNT-3):
        for col  in range(COLUMN_COUNT):
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece and board[row+3][col] == piece:
                return True
            
    # checking diagonally  (+ve sloped)
    for row in range(ROW_COUNT-3):
        for col  in range(COLUMN_COUNT-3):
            if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece and board[row+3][col+3] == piece:
                return True

    for col in range(COLUMN_COUNT-3):
        for row in range(3 , ROW_COUNT):
            if board[row][col] == piece and board[row-1][col+1] == piece and board[row-2][col+2] == piece and board[row-3][col+3] == piece:
                return True
        
    return False
        
    
"""
    # checking diagonally  (+ve sloped)
    X-----
    -X----
    --X---
    ------
    ------
    ------
    col - 3 , row - 3 
    
    after flip 
    ------
    ------
    ------
    --X---
    -X----
    X-----
    
    # checking diagonally  (-ve sloped)
    ------
    ------
    ------
    --X---
    -X----
    X-----
    3 -> row , col - 3 
    
    after flip 
    X-----
    -X----
    --X---
    ------
    ------
    ------
    
""" 

def draw_board():
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen , BLUE , (col*SQUARE_SIZE , row*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE , SQUARE_SIZE))
            pygame.draw.circle(screen , BLACK , (col*SQUARE_SIZE  +SQUARE_SIZE/2 , row* SQUARE_SIZE+SQUARE_SIZE + SQUARE_SIZE/2   ) , int(SQUARE_SIZE/2   - 5)   )
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.circle(screen , RED , (col*SQUARE_SIZE  +SQUARE_SIZE/2 , height - (row* SQUARE_SIZE+SQUARE_SIZE + SQUARE_SIZE/2)  + SQUARE_SIZE  ) , int(SQUARE_SIZE/2   - 5)   )
            elif board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (col*SQUARE_SIZE  +SQUARE_SIZE/2, height - (row* SQUARE_SIZE+SQUARE_SIZE + SQUARE_SIZE/2) + SQUARE_SIZE ), int(SQUARE_SIZE/2   - 5)   )
            
            
    
    pygame.display.update()
            
    
  
            
            
    
             


board  = create_board()
game_over = False 
turn = 0

print_board(board)





pygame.init()

width  = COLUMN_COUNT * SQUARE_SIZE
height =( ROW_COUNT + 1) * SQUARE_SIZE

size  = (width, height)

screen = pygame.display.set_mode(size)
draw_board()
pygame.display.update()



myfont = pygame.font.SysFont("monospace" , 75 ) 

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type ==  pygame.MOUSEMOTION:
            pygame.draw.rect(screen , BLACK  , (0,0, width , SQUARE_SIZE) )
            col = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen , RED , (col,SQUARE_SIZE/2 ), int(SQUARE_SIZE/2   - 5)   )
                
            else :
                pygame.draw.circle(screen, YELLOW, (col,SQUARE_SIZE/2 ), int(SQUARE_SIZE/2   - 5)   )
        pygame.display.update()
                
                
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen , BLACK  , (0,0, width , SQUARE_SIZE) )

            # print(event.pos)
            if turn == 0:
                posx = event.pos[0]
                col = int(posx / SQUARE_SIZE) 
 
                if is_Valid_location(board , col):
                    row = get_next_open_row(board, col)
                    if row!= -1:
                        drop_piece(board, row, col, 1)
                    if winning_move(board , 1 ):
                        label = myfont.render("Player 1 wins!!" , 1 ,RED)
                        screen.blit(label , (40,10))
                        game_over = True
                
            else : 
                posx = event.pos[0]
                col = int(posx / SQUARE_SIZE) 

                if is_Valid_location(board , col):
                    row = get_next_open_row(board, col)
                    if row!= -1:
                        drop_piece(board, row, col, 2)
                    if winning_move(board , 2 ):
                        label = myfont.render("Player 2 wins !!" , 1 ,RED)
                        screen.blit(label , (40,10))
                        game_over = True
            draw_board()
            
            

                    
            turn ^= 1 # this alernates the current turn """
            if game_over :
                pygame.time.wait(3000)