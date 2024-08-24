import turtle

game_screen = turtle.Screen()
game_screen.bgcolor("red")
game_screen.title("Turtle Game")

Franklin = turtle.Turtle()


#ScoreBoard

Franklin.speed(0)
Franklin.color("Black")
Franklin.penup()
Franklin.hideturtle()
Franklin.goto(0, 350)
score_a = 0
score_b = 0


def turtle_swichted_red():
    Franklin.clear()
    Franklin.write(f"You swichted Red  BLUE team: {score_b} ", align="center", font=("Courier", 24, "normal"))


def increase_score_red():
    global score_a
    score_a += 1
    turtle_swichted_red()
    change_color_white()
    change_color_score_board_blue()
    counter_black()
    time_counter_black()


def increase_score_blue():
    global score_b
    score_b += 1
    turtle_scorboard()
    change_color_black()
    change_color_score_board_red()
    counter_white()
    time_counter_white()


def change_color_white():
    game_screen = turtle.bgcolor("red")


def change_color_black():
    game_screen = turtle.bgcolor("blue")


def change_color_score_board_blue():
    Franklin.color("blue")


def change_color_score_board_red():
    Franklin.color("red")

    #turtle_scorboard()


#increase_score_white()
#increase_score_black()


turtle.listen()
turtle.onkey(fun=increase_score_red, key="w")
turtle.onkey(fun=increase_score_blue, key="b")

turtle_scorboard()

#counter

Percy = turtle.Turtle()

Percy.hideturtle()
Percy.penup()
Percy.goto(0, 300)

count = 0


def pery_counter():
    Percy.clear()
    Percy.write(f"Total Point: {count}", align="center", font=("Arial", 24, "normal"))


def counter_of_percy():
    global count
    count += 1
    pery_counter()


def counter_white():
    counter_of_percy()
    Percy.color("white")


def counter_black():
    counter_of_percy()
    Percy.color("black")


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

# don't pass here


game_screen.register_shape("eagle.gif.gif")  # Make sure the file is in the same directory

# Load and set the background image (your image)
image_path = "eagle.gif.gif"  # Replace with your GIF file name
game_screen.bgpic(image_path)  # Set the image as the background

image_left = 400  # X coordinate of the left edge of the image
image_right = -400  # X coordinate of the right edge of the image
image_bottom = -300  # Y coordinate of the bottom edge of the image
image_top = 300  # Y coordinate of the top edge of the image


score = 0

# Function to update the score when the image area is clicked
def update_score(x, y):
    global score
    # Check if the click is within the image area
    if image_left < x < image_right and image_bottom < y < image_top:
        score += 1
        Franklin.clear()
        Franklin.write(f"Score: {score}", align="left", font=("Arial", 24, "normal"))


# Bind the click event on the screen
game_screen.onscreenclick(update_score)

turtle.listen()

pery_counter()
turtle_scorboard()
increase_score_red()
increase_score_blue()
turtle_time()

turtle.mainloop()
