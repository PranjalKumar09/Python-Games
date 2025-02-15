"""
A tag is a string that you can associate with objects on the canvas.

A tag can be associated with any number of objects on the canvas, including zero.

An object can have any number of tags associated with it, including zero.

Tags have many uses. For example, if you are drawing a map on a canvas, and there are text objects for the labels on rivers, you could attach the tag 'riverLabel' to all those text objects. This would allow you to perform operations on all the objects with that tag, such as changing their color or deleting them

after(ms, function = None, *args)  # after this much time window will automatically come with these thing and function

canvas.delete(ALL) # deletes  every thing canvas_object linked to it

window.resizable(False, False) # height , width we cant resize 

"""


import random
from tkinter import *

GAME_WIDTH = 900
GAME_HEIGHT = 600
TIME = 100 #o.1 second
SPACE_SIZE = 25
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self) -> None: #here none does nothing but for better error message giving complete message 
        self.body_size = BODY_PARTS
        self.coordinates = []#it is list of list -> [[,], [,], [,]...]
        self.squares = [] 

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(#upper - left and down - right 
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up": # snake_head updating according to direction
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    else:
        x += SPACE_SIZE

    # updating coordinates in snake coordinates and snake square to make graphic of proceeding movement
    snake.coordinates.insert(0, (x, y))  

    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    )
    snake.squares.insert(0, square)
    
    # now checking whether food coordinates matches then upgrading score
    
    # if food match nothing it automatically create new food
    # else delete last index of food...

    if x == food.coordinates[0] and y == food.coordinates[1]: 

        global score

        score += 1
        label.config(text="Score: {}".format(score)) #updating new score

        canvas.delete("food")   #deleting old score

        food = Food()  #called new food material so new food come 
    else: #deleting last coordinate and square

        del snake.coordinates[-1] 

        canvas.delete(snake.squares[-1]) 

        del snake.squares[-1]

    if check_collisions(snake): #if collided then end game
        game_over()
    else:
        window.after(TIME, next_turn, snake, food)


def change_direction(new_direction):

    global direction #this direction is on next turn function
    
    # in on direction there is 2 option the direction in which it cant go is going back means opposite direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def game_over():
    canvas.delete(ALL) #deletes  every thing canvas_object linked to it
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=("consolas", 70),
        text="GAME OVER",
        fill="red",
    )


window = Tk()
window.title("Kumar Snake game")
window.resizable(False, False) ## height , width we cant resize 

#intial direction & score
score = 0
direction = "down"

label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))
#
window.bind("a", lambda event: change_direction("left"))
window.bind("d", lambda event: change_direction("right"))
window.bind("w", lambda event: change_direction("up"))
window.bind("s", lambda event: change_direction("down"))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
