
# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import turtle as trii

#-----game configuration----
timer = 15
counter_interval = 1000

def countdown():
  global timer, timer_up
  trtl.clear()
  if timer <= 0:
    trtl.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    trtl.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    trtl.getscreen().ontimer(countdown, counter_interval)
#-----initialize turtle-----
trii.color('yellow')
trii.hideturtle()
tri_color = "yellow"
tri_shape = "circle"
tri_size = "2"
tri = trtl.Turtle()
tri.color(tri_color)
tri.shapesize(int(tri_size))
tri.shape(tri_shape)
font_setup = ("Arial", 20, "normal")



#-----game functions--------

new_xpos = 0
new_ypos = 0
score = 0


timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

def countdown():
  global timer, timer_up
  tri.clear()
  if timer <= 0:
    trii.clear()
    trii.penup()
    trii.speed(0)
    trii.goto(200, 200)
    trii.speed(3)
    trii.clear()
    trii.pendown()
    trii.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    trii.clear()
    trii.penup()
    trii.speed(0)
    trii.goto(200, 200)
    trii.speed(3)
    trii.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    trii.getscreen().ontimer(countdown, counter_interval)
def change_position(x,y):
    tri.penup()
    global score
    score += 1
    tri.speed(0)
    tri.goto(-200, 200)
    tri.speed(3)
    tri.clear()
    tri.color('yellow')
    tri.write(score, font=font_setup)
    tri.hideturtle()
    new_xpos = rand.randint(0, 400)
    new_ypos = rand.randint(0, 300)
    colors = rand.choice(color)
    tri.color(colors)

    size = rand.choice(sizes)
    tri.shapesize(size)
    tri.goto(new_xpos, new_ypos)
    print(str(new_xpos) + ", " + str(new_ypos))
    
    tri.showturtle()
countdown()

sizes = [0.5, 0.75, 1, 1.25, 1.5]
color = ['red', 'blue', 'green', 'orange', 'purple', 'yellow',]

#-----events----------------
tri.onclick(change_position)
wn = trtl.Screen() 
wn.bgcolor('#8db3e2')
   
wn.mainloop()