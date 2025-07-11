## Make sure to Install Pillow and also put the (code file) and the (background file) in the same folder for the code to work

## How the game work
- A window with a basket at the bottom
- Falling “balls" (blue circles)
- Player uses arrow keys to move the basket
- When a ball touches the basket → score increases
- When a ball hits the ground → lose a life
- Three lives available
- If lives = 0 → Game Over

## Objective
Through this project, we will learn:
- How to use tkinter for building graphical user interfaces
- How to handle keyboard input and game loops
- How to implement collision detection and real-time game updates
- How to use Pillow to load and display custom background images



## Flowchart explanation
1. move_left Function
Start (Oval): Left key press.
Process (Rectangle): Move basket left 25 pixels.
End (Oval): Return to main loop.
2. move_right Function
Start (Oval): Right key press.
Process (Rectangle): Move basket right 25 pixels.
End (Oval): Return to main loop.
3. create_ball Function
Start (Oval): Create new ball.
Process (Rectangle): Random x (10-470).
Process (Rectangle): Create cyan oval at (x,0,x+30,30).
Process (Rectangle): Add ball to list.
Decision (Diamond): Game running?
Yes: Schedule create_ball (1500ms).
No: Skip.
End (Oval): Return to main loop.
4. move_balls Function
Start (Oval): Update balls.
Decision (Diamond): Game running?
No: End.
Yes:
Process (Rectangle): For each ball:
Move down 10 pixels.
Get coordinates.
Decision (Diamond): Bottom >= 700?
Yes:
Remove ball.
Delete ball.
Decrease lives.
Parallelogram: Update lives text.
Decision (Diamond): Lives == 0?
Yes:
Set game_running False.
Parallelogram: Show "Game Over".
End.
No: Next ball.
No:
Check collision.
Decision (Diamond): Collision?
Yes:
Increase score.
Parallelogram: Update score text.
Remove ball.
Delete ball.
No: Next ball.
Schedule move_balls (100ms).
End (Oval): Return to main loop.
5. check_collision Function
Start (Oval): Check ball, basket collision.
Process (Rectangle): Get ball coordinates.
Process (Rectangle): Get basket coordinates.
Decision (Diamond): Overlap?
Yes: Return True.
No: Return False.
End (Oval): Return result.
6. Main Program
Oval: Start.
Rectangle: Init Tkinter, set title, size, non-resizable.
Rectangle: Create canvas, load/display background.
Rectangle: Create basket, set score=0, lives=3, game_running=True.
Parallelogram: Show score, lives.
Rectangle: Bind Left/Right keys.
Rectangle: Call create_ball, move_balls.
Rectangle: Start main loop, handle:
Diamond: Left/Right key → move_left/move_right.
Rectangle: create_ball → Spawn balls.
Rectangle: move_balls → Update, check collisions.
Oval: End (window closed).
