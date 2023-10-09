"""
All the 'screen' starters will be displayed here:
"""

import turtle

#One only screen :
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor((125, 12, 145))
wn.setup(800, 900)
wn.title("Puzzle 15 By: Itay Shinderman")
wn.tracer(False)

#Draw the right square for the sprites :
turtle.pu()
turtle.goto(-200, 200)
turtle.pd()
for _ in range(4):
  turtle.fd(400)
  turtle.rt(90)

for _ in range(4):
  turtle.fd(400)
  turtle.setx(-200)
  turtle.sety(turtle.ycor() - 100)

turtle.seth(90)
for _ in range(4):
  turtle.fd(400)
  turtle.sety(-200)
  turtle.setx(turtle.xcor() + 100)

turtle.goto(50, 300)
turtle.pu()
turtle.ht()

