import tkinter as tk
import random

# Initialize the main window
WIDTH, HEIGHT = 400, 600
window = tk.Tk()
window.title("Flappy Bird")
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="sky blue")
canvas.pack()

# Game variables
bird_x, bird_y = WIDTH // 4, HEIGHT // 2
bird_size = 20
bird_velocity = 0
gravity = 0.5
jump_strength = -10

pipe_width = 70
pipe_gap = 200
pipe_speed = 5
pipes = []
score = 0
game_active = True

# Functions to handle bird movement and pipes
def create_pipe():
    pipe_height = random.randint(100, HEIGHT - 200)
    top_pipe = canvas.create_rectangle(WIDTH, 0, WIDTH + pipe_width, pipe_height, fill="green")
    bottom_pipe = canvas.create_rectangle(WIDTH, pipe_height + pipe_gap, WIDTH + pipe_width, HEIGHT, fill="green")
    pipes.append((top_pipe, bottom_pipe))

def move_pipes():
    global score, game_active
    pipes_to_remove = []
    
    for top_pipe, bottom_pipe in pipes:
        # Move pipes to the left
        canvas.move(top_pipe, -pipe_speed, 0)
        canvas.move(bottom_pipe, -pipe_speed, 0)
        
        # Check if the right edge of the pipe has moved off the screen
        if canvas.coords(top_pipe)[2] < 0:
            pipes_to_remove.append((top_pipe, bottom_pipe))  # Mark pipes for removal
            score += 1  # Increment score when a pair of pipes is passed
    
    # Remove pipes that are off-screen
    for top_pipe, bottom_pipe in pipes_to_remove:
        canvas.delete(top_pipe)
        canvas.delete(bottom_pipe)
        pipes.remove((top_pipe, bottom_pipe))  # Remove the pipe pair from the list

    # Add new pipes if necessary
    if not pipes or canvas.coords(pipes[-1][0])[2] < WIDTH - 200:
        create_pipe()


def check_collision():
    global game_active
    bird_coords = canvas.coords(bird)
    if bird_coords[1] <= 0 or bird_coords[3] >= HEIGHT:
        game_active = False
    
    for top_pipe, bottom_pipe in pipes:
        if canvas.bbox(bird) and (canvas.bbox(top_pipe) and canvas.bbox(bottom_pipe)):
            if (
                bird_coords[2] > canvas.coords(top_pipe)[0]
                and bird_coords[0] < canvas.coords(top_pipe)[2]
                and (bird_coords[1] < canvas.coords(top_pipe)[3] or bird_coords[3] > canvas.coords(bottom_pipe)[1])
            ):
                game_active = False

def update_game():
    global bird_velocity, game_active
    if game_active:
        bird_velocity += gravity
        canvas.move(bird, 0, bird_velocity)
        
        move_pipes()
        check_collision()
        
        # Update score display
        canvas.itemconfig(score_text, text=f"Score: {score}")
        window.after(30, update_game)
    else:
        canvas.create_text(WIDTH // 2, HEIGHT // 2, text="Game Over", font=("Arial", 24), fill="red")

def jump(event):
    global bird_velocity
    if game_active:
        bird_velocity = jump_strength
    else:
        reset_game()

def reset_game():
    global bird_velocity, pipes, score, game_active
    bird_velocity = 0
    canvas.coords(bird, bird_x, bird_y, bird_x + bird_size, bird_y + bird_size)
    for top_pipe, bottom_pipe in pipes:
        canvas.delete(top_pipe)
        canvas.delete(bottom_pipe)
    pipes = []
    score = 0
    game_active = True
    create_pipe()
    update_game()

# Create initial bird and pipe
bird = canvas.create_oval(bird_x, bird_y, bird_x + bird_size, bird_y + bird_size, fill="yellow")
score_text = canvas.create_text(10, 10, anchor="nw", font=("Arial", 18), text=f"Score: {score}")

# Set up event bindings and start the game
window.bind("<space>", jump)
create_pipe()
update_game()

window.mainloop()
