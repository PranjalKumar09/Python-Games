""" 



Problem 1 : Why sometime we have choosen row,col and sometimes col,row
same problem  in clear_rows why we used j,i instead of i,j


Function: create_grid
    It is designed to generate a color grid that represents the state of the play area in a Tetris game. It assigns colors to individual blocks based on the locked_positions parameter, providing a visual representation of the Tetris pieces on the screen.

    Parameters:
        locked_positions (default empty dictionary): A dictionary containing information about the positions and colors of locked Tetris pieces.

    Return Value:
        grid: A 2D list representing the color of each block in the play area. Each element is a tuple (r, g, b) indicating the color of the corresponding block.

    Implementation:
        Initialization:
            num_blocks_width and num_blocks_height are calculated based on the play area dimensions and block size.
            grid is initialized with default color (0, 0, 0) for all blocks.

        Color Assignment:
            The function then iterates through each block in the play area.
            If a block is part of a locked Tetris piece (found in locked_positions), its color is updated to the specified color in the dictionary.

        Result:
            The final grid represents the colored blocks in the play area, where the default color (0, 0, 0) denotes an empty block, and other colors represent locked Tetris pieces.

    Note:
        Although named create_grid, this function is primarily responsible for creating the color representation of individual blocks rather than a traditional grid structure. The color information is crucial for rendering the Tetris game graphics accurately.







FUNCTION convert_shape_format(piece):
    
    Converts the current shape and position of a TetrisPiece into a list of grid positions
    representing the occupied blocks.

    Parameters:
    - piece (TetrisPiece): The Tetris piece for which the shape and position need to be converted.

    Returns:
    - List[(int, int)]: A list of (x, y) coordinates representing the occupied blocks on the grid.
    

    # 1. Initialize an empty list to store block positions in     postions = [ (x,y) , ...]

    # 2. Retrieve the current shape of the Tetris piece based on its rotation. (len done to be on limit)

    # 3. Iterate through each line of the shape.
        # 4. Convert the line to a list for easier iteration.
        # 5. Iterate  each character (column) in  line.
            # 6. If the character is '0', add the block position to the list.

    # 7. Adjustment x-2 , y-4

    # 8. return positions



"""


import pygame
import random
import sys 

pygame.font.init()

# Global Variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
PLAY_WIDTH = 300  # 300/30 = 10
PLAY_HEIGHT = 600  # 600/30 = 20
BLOCK_SIZE = 30
PLAY_AREA_X = (SCREEN_WIDTH - PLAY_WIDTH) // 2
PLAY_AREA_Y = SCREEN_HEIGHT - PLAY_HEIGHT

# Shape Formats
S_SHAPE = [
    ['.....',
     '.....',
     '..00.',
     '.00..',
     '.....'],
    ['.....',
     '..0..',
     '..00.',
     '...0.',
     '.....']]
Z_SHAPE = [
    ['.....',
     '.....',
     '.00..',
     '..00.',
     '.....'],
    ['.....',
     '..0..',
     '.00..',
     '.0...',
     '.....']
]
I_SHAPE = [
    ['..0..',
     '..0..',
     '..0..',
     '..0..',
     '.....'],
    ['.....',
     '0000.',
     '.....',
     '.....',
     '.....']
]
O_SHAPE = [
    ['.....',
     '.....',
     '.00..',
     '.00..',
     '.....']
]
J_SHAPE = [
    ['.....',
     '.0...',
     '.000.',
     '.....',
     '.....'],
    ['.....',
     '..00.',
     '..0..',
     '..0..',
     '.....'],
    ['.....',
     '.....',
     '.000.',
     '...0.',
     '.....'],
    ['.....',
     '..0..',
     '..0..',
     '.00..',
     '.....']
]
L_SHAPE = [
    ['.....',
     '...0.',
     '.000.',
     '.....',
     '.....'],
    ['.....',
     '..0..',
     '..0..',
     '..00.',
     '.....'],
    ['.....',
     '.....',
     '.000.',
     '.0...',
     '.....'],
    ['.....',
     '.00..',
     '..0..',
     '..0..',
     '.....']
]
T_SHAPE = [
    ['.....',
     '..0..',
     '.000.',
     '.....',
     '.....'],
    ['.....',
     '..0..',
     '..00.',
     '..0..',
     '.....'],
    ['.....',
     '.....',
     '.000.',
     '..0..',
     '.....'],
    ['.....',
     '..0..',
     '.00..',
     '..0..',
     '.....']
]

SHAPES = [S_SHAPE, Z_SHAPE, I_SHAPE, O_SHAPE, J_SHAPE, L_SHAPE, T_SHAPE]
SHAPE_COLORS = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

class TetrisPiece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.rotation = 0 # rotation from 0 -
def create_grid(locked_positions={}):
    num_blocks_width = PLAY_WIDTH // BLOCK_SIZE
    num_blocks_height = PLAY_HEIGHT // BLOCK_SIZE
    grid = [[(0, 0, 0) for _ in range(num_blocks_width)] for _ in range(num_blocks_height)]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            current_position = (col, row)
            if current_position in locked_positions:
                color_at_position = locked_positions[current_position]
                grid[row][col] = color_at_position

    return grid
def convert_shape_format(piece):
    positions = []
    current_format = piece.shape[piece.rotation % len(piece.shape)]

    for index, line in enumerate(current_format):
        row = list(line)
        for j_index, column in enumerate(row):
            if column == '0':
                positions.append((piece.x + j_index, piece.y + index))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4) # y is falling from negative at starting 

    return positions
def is_valid_shape(piece, block_colors_grid):
    accepted_positions = [
        [(row, col) for row in range(len(block_colors_grid[0])) if block_colors_grid[col][row] == (0, 0, 0)] for col in range(len(block_colors_grid))
    ]

    accepted_positions = [pos for sub in accepted_positions for pos in sub] # this line is just converitng upper 2d list in 1d

    formatted_positions = convert_shape_format(piece)
    for pos in formatted_positions:
        if (pos not in accepted_positions) and pos[1] > -1:
            return False

    return True
def has_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
def get_random_shape():
    initial_x = (PLAY_WIDTH // BLOCK_SIZE) // 2  # Centered horizontally
    return TetrisPiece(initial_x, 0, random.choice(SHAPES))
def draw_text_middle(surface ,text ,size, color):
    font = pygame.font.SysFont("Comicaans" , size , bold = True )
    title_label = font.render(text , 1  , color)
    surface.blit(title_label , (PLAY_AREA_X + PLAY_WIDTH / 2 - title_label.get_width() / 2 , PLAY_AREA_Y + PLAY_HEIGHT / 2  - title_label.get_height()/2))
def draw_grid(display_surface, block_colors_grid):
    current_x = PLAY_AREA_X
    current_y = PLAY_AREA_Y

    medium_grey_color = (128, 128, 128)
    for row_index in range(len(block_colors_grid)):
        y = current_y + row_index * BLOCK_SIZE
        pygame.draw.line(display_surface, medium_grey_color, (current_x, y), (current_x + PLAY_WIDTH, y))

        for col_index in range(len(block_colors_grid[row_index])):
            x = current_x + col_index * BLOCK_SIZE
            pygame.draw.line(display_surface, medium_grey_color, (x, current_y), (x, current_y + PLAY_HEIGHT))
def clear_rows(grid , locked_positions):
    """ 
    
    locked_postion is dictionary => { (x,y) : color}"""
    
    
    
    
    # need to see if row is clear the shift every other row above down one
 
    inc = 0
    for i in range(len(grid)-1,-1,-1):# looks grid backwards
        row = grid[i]
        if (0, 0, 0) not in row: # if no empty place
            inc += 1
            # add positions to remove from locked
            ind = i  # we are removing from bacward (i)
            for j in range(len(row)): 
                try:
                    del locked_positions[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked_positions), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked_positions[newKey] = locked_positions.pop(key)
    return inc # inc is how much rows we are clearing 
def draw_next_shape(piece, display_surface):
    font = pygame.font.SysFont('comicsans', BLOCK_SIZE * 2)
    title_label = font.render('Next', 1, (255, 255, 255))
    sx = PLAY_AREA_X + PLAY_WIDTH + 50
    sy = PLAY_AREA_Y + PLAY_HEIGHT/2 - 100
    format = piece.shape[piece.rotation % len(piece.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(display_surface, piece.color, (sx + j*BLOCK_SIZE, sy + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
 
    display_surface.blit(title_label, (sx + 10, sy- 30))

def draw_window(display_surface, block_colors_grid, score=0 , last_score= 0 ):
    display_surface.fill((0, 0, 0))
    font = pygame.font.SysFont('comicsans', BLOCK_SIZE * 2)
    title_label = font.render('Tetris', 1, (255, 255, 255))
    display_surface.blit(title_label, (PLAY_AREA_X + PLAY_WIDTH / 2 - title_label.get_width() / 2, BLOCK_SIZE))

    # current score  
    title_label = font.render('Score : ', 1, (255, 255, 255))
    display_surface.blit(title_label, (PLAY_AREA_X + PLAY_WIDTH + 50 , PLAY_AREA_Y + PLAY_HEIGHT/2  + 42))
    
    title_label = font.render(str(score), 1, (255, 255, 255))
    display_surface.blit(title_label, (PLAY_AREA_X + PLAY_WIDTH + 50 , PLAY_AREA_Y + PLAY_HEIGHT/2  + 75))
    
   
   
    # last score 
    title_label = font.render('Last Score : ' , 1, (255, 255, 255))
    display_surface.blit(title_label, (10 , PLAY_AREA_Y + PLAY_HEIGHT/2  + 42))
    title_label = font.render(str(last_score), 1, (255, 255, 255))
    display_surface.blit(title_label, (15 , PLAY_AREA_Y + PLAY_HEIGHT/2  + 75))
    
    
    for row_index in range(len(block_colors_grid)):
        for col_index in range(len(block_colors_grid[row_index])):
            block_color = block_colors_grid[row_index][col_index]
            block_x = PLAY_AREA_X + col_index * BLOCK_SIZE
            block_y = PLAY_AREA_Y + row_index * BLOCK_SIZE
            pygame.draw.rect(display_surface, block_color, (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE), 0)
    draw_grid(display_surface, block_colors_grid)
    pygame.draw.rect(display_surface, (255, 0, 0), (PLAY_AREA_X, PLAY_AREA_Y, PLAY_WIDTH, PLAY_HEIGHT), 5)
"""   block_x: The x-coordinate of the top-left corner of the rectangle.
    block_y: The y-coordinate of the top-left corner of the rectangle.
    BLOCK_SIZE: The width of the rectangle.
    BLOCK_SIZE: The height of the rectangle. """
def update_score(nscore):
    score = max_score()
    with open('Projects/TERTIS_GAME/scores.txt', 'r') as f:
        line = f.readlines()
        score = line[0].strip()
    with open('Projects/TERTIS_GAME/scores.txt', 'w') as f:
        if int(score) > nscore : 
            f.write(str(score))
        else :f.write(str (nscore))
def max_score():
    with open('Projects/TERTIS_GAME/scores.txt', 'r') as f:
        line = f.readlines()
        score = line[0].strip()
    return int(score)
def main(display_surface):
    last_Score =  max_score()
    locked_positions = {}

    change_piece = False
    run = True
    current_piece = get_random_shape()
    next_piece = get_random_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    level_time = 0
    fall_speed = 0.27
    score = 0 

    while run:
        grid = create_grid(locked_positions) # it returns 2d list of block colores
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()
        
        if level_time / 1000 > 5:
            level_time = 0
            if fall_speed > 0.12:
                fall_speed -= 0.005
                


        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (is_valid_shape(current_piece, grid) and current_piece.y > 0):
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not is_valid_shape(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not is_valid_shape(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not is_valid_shape(current_piece, grid):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not is_valid_shape(current_piece, grid):
                        current_piece.rotation -= 1

        shape_positions = convert_shape_format(current_piece)

        for i, pos in enumerate(shape_positions):
            x, y = pos
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_positions:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color

            current_piece = next_piece
            next_piece = get_random_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions)*10 # clearing rows when change piece or piece change touch ground 
            

        draw_window(display_surface, grid, score , last_Score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if has_lost(locked_positions):
            draw_text_middle(win , "YOU LOST!" , 80, (255 , 255, 255))
            pygame.display.update()
            pygame.time.delay(1500)
            update_score(score)
            
            
            
        

    pygame.display.quit()

def main_menu(win):
    win.fill((0,0,0))
    draw_text_middle(win , "PRESS ANY KEY TO START " ,60, (255,255,255))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                return


                
                

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tertis")
main_menu(win)
# Then start the game
main(win)