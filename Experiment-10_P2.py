import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.bgcolor("#FFFFFF")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.width(3)
t.up()

colors = ["#FF9933", "#FFFFFF", "#138808"]
for i in range(3):
    t.color(colors[i])
    t.begin_fill()
    t.goto(-250, 150 - i * 100)
    t.down()
    t.goto(250, 150 - i * 100)
    t.goto(250, 50 - i * 100)
    t.goto(-250, 50 - i * 100)
    t.goto(-250, 150 - i * 100)
    t.end_fill()
    t.up()


t.goto(0, 0)
t.circle(50,5)
t.color("#000080")
t.down()
for i in range(24):
    t.forward(50)
    t.backward(50)
    t.right(15)
t.up()



t.hideturtle()
screen.mainloop()

'''
import turtle

# Create a turtle object 't' and set initial properties
t = turtle.Turtle()
t.speed("fastest")
t.penup()
t.goto(-100, -100)
t.pendown()

# Draw the base of the house
t.color("blue")
t.begin_fill()
for _ in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()

# Draw the roof
t.color("yellow")
t.begin_fill()
for _ in range(3):
    t.forward(200)
    t.left(120)
t.end_fill()

# Draw the door
t.penup()
t.goto(0, -100)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(2):
    t.forward(60)
    t.left(90)
    t.forward(100)
    t.left(90)
t.end_fill()

# Draw the flagpole
t.penup()
t.goto(50, 100)
t.pendown()
t.color("black")
t.pensize(5)
t.goto(50, 200)

# Draw the flag
t.penup()
t.goto(50, 200)
t.pendown()
t.color("red")
t.begin_fill()
for _ in range(2):
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Display the drawing
turtle.done()
'''