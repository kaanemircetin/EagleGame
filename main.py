import turtle
import random

game_screen = turtle.Screen()
game_screen.bgcolor("red")
game_screen.title("Eagle Game")

game_turtle = turtle.Turtle()

#Switch

game_turtle.speed(0)
game_turtle.color("Black")
game_turtle.penup()
game_turtle.hideturtle()
game_turtle.goto(0, 350)
score_a = 0
score_b = 0


def turtle_switched_red():
    game_turtle.clear()
    game_turtle.write(f"You Switched Red  ", align="center", font=("Courier", 24, "normal"))


def turtle_switched_blue():
    game_turtle.clear()
    game_turtle.write(f"You Switched Blue  ", align="center", font=("Courier", 24, "normal"))


def increase_score_red():
    global score_a
    score_a += 1
    turtle_switched_red()
    change_color_white()
    change_color_score_board_blue()
    counter_black()
    time_counter_black()


def increase_score_blue():
    global score_b
    score_b += 1
    turtle_switched_blue()
    change_color_black()
    change_color_score_board_red()
    counter_white()
    time_counter_white()


def change_color_white():
    game_screen = turtle.bgcolor("red")


def change_color_black():
    game_screen = turtle.bgcolor("blue")


def change_color_score_board_blue():
    game_turtle.color("blue")


def change_color_score_board_red():
    game_turtle.color("red")


turtle.listen()
turtle.onkey(fun=increase_score_red, key="r")
turtle.onkey(fun=increase_score_blue, key="b")

turtle_switched_blue()
turtle_switched_red()

#counter

game_counter = turtle.Turtle()

game_counter.hideturtle()
game_counter.penup()
game_counter.goto(0, 300)

count = 0


def my_game_counter():
    game_counter.clear()
    game_counter.write(f"Total Switch: {count}", align="center", font=("Arial", 24, "normal"))


def counter_of_percy():
    global count
    count += 1
    my_game_counter()


def counter_white():
    counter_of_percy()
    game_counter.color("white")


def counter_black():
    counter_of_percy()
    game_counter.color("black")


time_counter = turtle.Turtle()
time_counter.hideturtle()
time_counter.penup()
time_counter.goto(0, 250)

time_second = 0


def turtle_time():
    global time_second
    time_counter.clear()
    time_counter.write(f"Time: {time_second} seconds", align="center", font=("Arial", 24, "normal"))
    time_second += 1
    game_screen.ontimer(turtle_time, 1000)


def time_counter_white():
    time_counter.color("white")


def time_counter_black():
    time_counter.color("black")



# moving image
game_screen.addshape("eagle.gif.gif")

# First you should create a turtle object
moving_eagle = turtle.Turtle()
moving_eagle.shape("eagle.gif.gif")
moving_eagle.penup()

# You can create a turtle to display the score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, game_screen.window_height() // 2 - 250)
score_display.write("Score: 0", align="center", font=("Arial", 30, "normal"))


score = 0



def update_score(x, y):
    global score
    score += 1
    score_display.clear()  # Clear the previous score
    score_display.write(f"Score: {score}", align="center", font=("Arial", 30, "normal"))


# Function to move the eagle to a random location
def move_eagle_randomly():
    # If you want a teleport system you should hide the moving eagle before moving
    moving_eagle.hideturtle()

    # You can generate random coordinates within the screen boundaries
    x = random.randint(-game_screen.window_width() // 2 + 10, game_screen.window_width() // 2 - 10)
    y = random.randint(-game_screen.window_height() // 2 + 10, game_screen.window_height() // 2 - 10)

    # You can move the moving eagle to the new coordinates
    moving_eagle.goto(x, y)

    # You can show the moving eagle at the new location
    moving_eagle.showturtle()

    # Schedule the next move
    game_screen.ontimer(move_eagle_randomly, 1000)  # Move every 1000 milliseconds


# You can set up the click event to update the score
moving_eagle.onclick(update_score)




turtle.listen()

my_game_counter()
turtle_switched_blue()
turtle_switched_red()
increase_score_red()
increase_score_blue()
turtle_time()
move_eagle_randomly()

turtle.mainloop()
