import tkinter as tk
import random

# Game setup
GRID_SIZE = 20
CELL_SIZE = 20
WINDOW_WIDTH = GRID_SIZE * CELL_SIZE
WINDOW_HEIGHT = GRID_SIZE * CELL_SIZE

root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="pink")
canvas.pack()

# Snake setup
snake = [(10, 10), (9, 10), (8, 10)]
food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
direction = "right"
score = 0

# Game logic
def move_snake():
    global snake, food, direction, score

    # Move the snake
    head = snake[0]
    if direction == "up":
        new_head = (head[0], head[1] - 1)
    elif direction == "down":
        new_head = (head[0], head[1] + 1)
    elif direction == "left":
        new_head = (head[0] - 1, head[1])
    else:
        new_head = (head[0] + 1, head[1])

    snake.insert(0, new_head)

    # Check for collision
    if (
        new_head[0] < 0 or new_head[0] >= GRID_SIZE or
        new_head[1] < 0 or new_head[1] >= GRID_SIZE or
        new_head in snake[1:]
    ):
        game_over()
        return

    # Eat food
    if new_head == food:
        score += 1
        food = (random.randint(0, GRID_SIZE-1), random.randint(0, GRID_SIZE-1))
    else:
        snake.pop()

    # Redraw the game
    canvas.delete("all")
    canvas.create_rectangle(food[0]*CELL_SIZE, food[1]*CELL_SIZE, (food[0]+1)*CELL_SIZE, (food[1]+1)*CELL_SIZE, fill="white", outline="")
    for segment in snake:
        canvas.create_rectangle(segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, (segment[0]+1)*CELL_SIZE, (segment[1]+1)*CELL_SIZE, fill="white", outline="")
    canvas.create_text(10, 10, anchor="nw", text=f"Score: {score}", fill="white", font=("Arial", 12))

    root.after(100, move_snake)

def game_over():
    canvas.delete("all")
    canvas.create_text(WINDOW_WIDTH//2, WINDOW_HEIGHT//2, text=f"Game Over! Your score: {score}", fill="white", font=("Arial", 24))

# User input
def change_direction(event):
    global direction
    if event.keysym == "Up" and direction != "down":
        direction = "up"
    elif event.keysym == "Down" and direction != "up":
        direction = "down"
    elif event.keysym == "Left" and direction != "right":
        direction = "left"
    elif event.keysym == "Right" and direction != "left":
        direction = "right"

root.bind("<Key>", change_direction)

# Game loop
move_snake()
root.mainloop()
