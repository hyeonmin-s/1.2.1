# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
color = "red"
size = 2
shape = "circle"
score = 0

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(shape)
spot.shapesize(size)
spot.fillcolor(color)
spot.penup()
spot.speed(0)

#-----game functions--------
def spot_clicked(x,y):
  spot.hideturtle()
  change_position()
  spot.showturtle()

def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)

#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.mainloop()

aaaaaaa