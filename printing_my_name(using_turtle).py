import turtle

name = turtle.Turtle()

turtle.bgcolor("black")

name.pensize(10)
name.color("white")

#it displays letter 'S'
name.penup()
name.goto(-250, 200)
name.pendown()
name.goto(-350, 200)
name.goto(-350, 135)
name.goto(-250, 135)
name.goto(-250, 70)
name.goto(-350, 70)

#it displays letter 'A'
name.penup()
name.goto(-150, 200)
name.pendown()
name.goto(-225, 200)
name.goto(-225, 70)
name.goto(-225, 135)
name.goto(-150, 135)
name.goto(-150, 200)
name.goto(-150,70)

#it diplays letter 'G'
name.penup()
name.goto(-30, 200)
name.pendown()
name.goto(-125, 200)
name.goto(-125, 70)
name.goto(-30, 70)
name.goto(-30, 135)
name.goto(-70, 135)

#it diplays letter 'A'
name.penup()
name.goto(75, 200)
name.pendown()
name.goto(0, 200)
name.goto(0, 70)
name.goto(0, 135)
name.goto(75, 135)
name.goto(75, 200)
name.goto(75, 70)

#it diplays letter 'R'
name.penup()
name.goto(100, 200)
name.pendown()
name.goto(100, 70)
name.goto(100, 200)
name.goto(175, 200)
name.goto(175, 135)
name.goto(100, 135)
name.goto(175, 70)

name.color("white", "white")

turtle.done()
