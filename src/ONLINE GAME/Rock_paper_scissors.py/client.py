""" 
in python we can even put conditions like => y1 < x < y2  which not causes not error



Main Game Loop (main function):
    Initialize the network connection and get the player number.
    Enter a continuous loop to update the game state based on user input and network communication.
    Check for events such as quitting the game or clicking a button.
    Send the player's move over the network when a button is clicked.
    Receive updates from the network about the opponent's moves and game state.
    Continuously update the game display based on the received game state.

Menu Screen (menu_screen function):
    Display the menu screen with a prompt to start the game.
    Wait for the user to click to start the game.

Game State Updates:
    Continuously update the game state based on user input events and network updates.
    Display the player's move, opponent's move, and game status (e.g., waiting for opponent, game result) on the game window.

Game Over Handling:
    When the game is over (e.g., both players have played), display the result and wait for a delay before resetting the game.

"""


import pygame
from Network import Network

# Initialize pygame
pygame.font.init()

# Global constants for window dimensions
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

# Global colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Initialize window
pygame.display.set_caption("Rock Paper Scissors")
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Global font
FONT = pygame.font.SysFont("comicsans", 40)

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        text = FONT.render(self.text, 1, WHITE)
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), 
                        self.y + round(self.height/2) - round(text.get_height()/2)))

    def is_clicked(self, pos):
        x1, y1 = pos
        return self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height

def redraw_window(game, player):
    win.fill(GRAY)

    if not game.connected():
        render_text("Waiting for Player...", RED, 80, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    else:
        render_text("Your Move", GREEN, 60, WINDOW_WIDTH * 0.1, WINDOW_HEIGHT * 0.2)
        render_text("Opponents", GREEN, 60, WINDOW_WIDTH * 0.55, WINDOW_HEIGHT * 0.2)

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.both_players_played():
            render_text(move1, BLACK, 60, WINDOW_WIDTH * 0.15, WINDOW_HEIGHT * 0.5)
            render_text(move2, BLACK, 60, WINDOW_WIDTH * 0.65, WINDOW_HEIGHT * 0.5)
        else:
            render_text(move1 if game.player1_has_played and player == 0 else "Locked In" if game.player1_has_played else "Waiting...",
                        BLACK, 60, WINDOW_WIDTH * 0.15, WINDOW_HEIGHT * 0.5)
            render_text(move2 if game.player2_has_played and player == 1 else "Locked In" if game.player2_has_played else "Waiting...",
                        BLACK, 60, WINDOW_WIDTH * 0.65, WINDOW_HEIGHT * 0.5)

        for btn in buttons:
            btn.draw(win)

    pygame.display.update()

def render_text(text, color, size, x, y):
    font = pygame.font.SysFont("comicsans", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    win.blit(text_surface, text_rect)

buttons = [Button("Rock", 50, 500, BLACK), Button("Scissors", 250, 500, RED), Button("Paper", 450, 500, GREEN)]

def main():
    run = True
    clock = pygame.time.Clock()
    network = Network()
    player = int(network.get_player_number())
    print("You are player", player)

    while run:
        clock.tick(60)
        try:
            game = network.send_data("get")
        except Exception as e:
            run = False
            print(f"Couldn't get game: {e}")
            break

        if game.both_players_played():
            redraw_window(game, player)
            pygame.time.delay(500)
            try:
                game = network.send_data("reset")
            except Exception as e:
                run = False
                print(f"Couldn't get game: {e}")
                break

            font = pygame.font.SysFont("comicsans", 90)
            if (game.determine_winner() == 1 and player == 1) or (game.determine_winner() == 0 and player == 0):
                render_text("You Won!", RED, 90, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            elif game.determine_winner() == -1:
                render_text("Tie Game!", RED, 90, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            else:
                render_text("You Lost...", RED, 90, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

            pygame.display.update()
            pygame.time.delay(2000) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in buttons:
                    if btn.is_clicked(pos) and game.connected():
                        if player == 0 and not game.player1_has_played:
                            network.send_data(btn.text)
                        elif player == 1 and not game.player2_has_played:
                            network.send_data(btn.text)

        redraw_window(game, player)

def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill(GRAY)
        render_text("Click to Play!", RED, 60, WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()

while True:
    menu_screen()
