import tkinter as tk
import random
from PIL import Image, ImageTk

# Set up main window
root = tk.Tk()
root.title("Catch the Balls")
root.geometry("500x700")
root.resizable(False, False)

canvas = tk.Canvas(root, width=500, height=700, bg="skyblue")
canvas.pack()

bg_img = Image.open("Background.jpg")
bg_img = bg_img.resize((500, 700))
bg_tk = ImageTk.PhotoImage(bg_img)
canvas.create_image(0, 0, anchor="nw", image=bg_tk)

# Game variables
balls = []
score = 0
lives = 5
game_running = True

# Player basket
basket = canvas.create_rectangle(150, 650, 250, 670, fill="brown")

# Score display
score_text = canvas.create_text(10, 10, anchor="nw", font=("Arial", 16), text=f"Score: {score}")
lives_text = canvas.create_text(400, 10, anchor="nw", font=("Arial", 16), text=f"Lives: {lives}")

# Move basket
def move_left(event):
    canvas.move(basket, -25, 0)

def move_right(event):
    canvas.move(basket, 25, 0)

#Bind key
canvas.bind_all("<Left>", move_left)
canvas.bind_all("<Right>", move_right)

# Create a falling ball
def create_ball():
    x = random.randint(10, 470)
    ball = canvas.create_oval(x, 0, x+30, 30, fill="#00FFEE")
    balls.append(ball)
    #create ball every 1.5 seconds
    if game_running:
        root.after(1500, create_ball)

# Move ball down and check for collision
def move_balls():
    global score, lives, game_running

    for ball in balls[:]:
        canvas.move(ball, 0, 10)
        pos = canvas.coords(ball)

        if pos[3] >= 700:  # bottom
            balls.remove(ball)
            canvas.delete(ball)
            lives -= 1
            canvas.itemconfig(lives_text, text=f"Lives: {lives}")
            if lives == 0:
                game_running = False
                canvas.create_text(250, 300, text="Game Over", font=("Arial", 24), fill="red")
                return
        elif check_collision(ball, basket):
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")
            balls.remove(ball)
            canvas.delete(ball)
    #Move down every 0.1 seconds
    if game_running:
        root.after(100, move_balls)

# Check collision between two objects
def check_collision(obj1, obj2):
    pos1 = canvas.coords(obj1)
    pos2 = canvas.coords(obj2)
    overlap = not (pos1[2] < pos2[0] or pos1[0] > pos2[2] or pos1[3] < pos2[1] or pos1[1] > pos2[3])
    return overlap

# Start the game loop
create_ball()
move_balls()

root.mainloop()
