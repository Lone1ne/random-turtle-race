#SKETCH

# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(10)
# def move_back():
#     tim.backward(10)
# def turn_left():
#     tim.left(10)
# def turn_right():
#     tim.right(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_back, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()


from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle won!")
            else:
                print(f"You Lose. The {winning_color} turtle won.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)






screen.exitonclick()