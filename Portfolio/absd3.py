import turtle
turtle.speed(10)
turtle.pensize(3)
def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('black', 'red')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)

func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()


def txt():
    turtle.up()
    turtle.setpos(-40, 100)
    turtle.down()
    turtle.color('black')
    turtle.write("Haker_uz",font=("verdana",12,"bold"))

txt()
turtle.done()