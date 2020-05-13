import turtle

hexagon = turtle.Turtle()

def spiral():
   for i in range(50):
      hexagon.width(i / 25 + 1)
      hexagon.fd(i)
      hexagon.lt(59)

spiral()

hexagon.lt(70)
hexagon.fd(300)
spiral()

hexagon.lt(70)
hexagon.fd(300)
spiral()

hexagon.lt(70)
hexagon.fd(300)
spiral()

hexagon.lt(70)
hexagon.fd(300)
spiral()

hexagon.lt(75)
hexagon.fd(350)

turtle.done()