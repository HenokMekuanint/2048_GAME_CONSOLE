import turtle
import datetime
from turtle import Screen

# the background
turtle.bgcolor("silver")
turtle.speed(50)
turtle.hideturtle()
animation=Screen()

#the box
box=turtle.Turtle()
box.speed(50)
box.hideturtle()
box.penup()
box.goto(0,-250)
box.pendown()
box.fillcolor("#030303")
box.begin_fill()
box.forward(250)
box.left(90)
box.forward(500)
box.left(90)
box.forward(500)
box.left(90)
box.forward(500)
box.left(90)
box.forward(250)
box.end_fill()

#filling the circle with color
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.hideturtle()
turtle.fillcolor("#141414")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

#the border circle
border=turtle.Turtle()
border.speed(50)
border.pensize(15)
border.penup()
border.goto(0,-200)
border.pendown()
border.color("brown")
border.circle(200)
#the hour lines on the clock
arrow1=turtle.Turtle()
arrow1.speed(50)
arrow1.hideturtle()
arrow1.color("blue")
arrow1.width(5)
arrow1.right(270)
i=12
while i>=1:
    arrow1.penup()
    arrow1.forward(150)
    arrow1.pendown()
    arrow1.forward(50)
    arrow1.penup()
    arrow1.goto(0,0)
    arrow1.left(30)
    arrow1.pendown()
    arrow1.color("blue")
    i-=1
#the minute pointer
i=0
arrow2=turtle.Turtle()
arrow2.hideturtle()
arrow2.speed(200)
arrow2.color("blue")
arrow2.width(3)
while i<60:
    arrow2.penup()
    arrow2.forward(170)
    arrow2.pendown()
    arrow2.forward(30)
    arrow2.penup()
    arrow2.goto(0,0)
    arrow2.left(6)

    i+=1

#the numbers on the clock
num=turtle.Turtle()
num.speed(50)
num.hideturtle()
num.penup()
num.goto(-15,120)
num.pendown()
num.color("orange")
num.write("12", font=("Times New Roman",30, "bold"))

num.penup()
num.goto(60,100)
num.pendown()
num.color("orange")
num.write("1", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(115,50)
num.pendown()
num.color("orange")
num.write("2", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(130,-20)
num.pendown()
num.color("orange")
num.write("3", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(110,-90)
num.pendown()
num.color("orange")
num.write("4", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(60,-135)
num.pendown()
num.color("orange")
num.write("5", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(-10,-155)
num.pendown()
num.color("orange")
num.write("6", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(-70,-140)
num.pendown()
num.color("orange")
num.write("7", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(-125,-95)
num.pendown()
num.color("orange")
num.write("8", font=("Times New Roman", 30, "bold"))


num.penup()
num.goto(-150,-20)
num.pendown()
num.color("orange")
num.write("9", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(-145,35)
num.pendown()
num.color("orange")
num.write("10", font=("Times New Roman", 30, "bold"))

num.penup()
num.goto(-95,100)
num.pendown()
num.color("orange")
num.write("11", font=("Times New Roman", 30, "bold"))

#geez numbers
num=turtle.Turtle()
num.speed(100)
num.hideturtle()
num.penup()
num.goto(-15,215)
num.pendown()
num.color("orange")
num.write("፲፪", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(110,175)
num.pendown()
num.color("orange")
num.write("፩", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(180,105)
num.pendown()
num.color("orange")
num.write("፪", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(210,-20)
num.pendown()
num.color("orange")
num.write("፫", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(180,-130)
num.pendown()
num.color("orange")
num.write("፬", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(110,-210)
num.pendown()
num.color("orange")
num.write("፭", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(-10,-240)
num.pendown()
num.color("orange")
num.write("፮", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(-120,-210)
num.pendown()
num.color("orange")
num.write("፯", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(-200,-130)
num.pendown()
num.color("orange")
num.write("፰", font=("Times New Roman", 20, "bold"))


num.penup()
num.goto(-225,-20)
num.pendown()
num.color("orange")
num.write("፱", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(-200,100)
num.pendown()
num.color("orange")
num.write("፲", font=("Times New Roman", 20, "bold"))

num.penup()
num.goto(-130,180)
num.pendown()
num.color("orange")
num.write("፲፩", font=("Times New Roman", 20, "bold"))

def revolution_of_hour():
   chour= datetime.datetime.now().hour
   revolvment = chour*-30+450
   cminute= datetime.datetime.now().minute
   revolvment = revolvment + (-1* cminute)/2
   hour.setheading(revolvment)
   animation.ontimer(revolution_of_hour, 60000)

#moving the minute using function
def revolution_of_minute():
    cminute= datetime.datetime.now().minute
    revolvment = cminute*-6+90
    csecond= datetime.datetime.now().second
    revolvment = revolvment + (csecond)*(-1/10)
    minute.setheading(revolvment)
    animation.ontimer(revolution_of_minute, 1000)

#moving the second using function
def revolution_of_second():
    csecond= datetime.datetime.now().second
    revolvment = csecond*-6+90
    second.setheading(revolvment)
    animation.ontimer(revolution_of_second, 1000)

#the hour pointer
hour=turtle.Turtle()
hour.shape("arrow")
hour.speed(50)
hour.color("green")
hour.shapesize(stretch_wid=0.4, stretch_len=5)


#the minute pointer
minute =turtle.Turtle()
minute.shape("arrow")
minute.speed(50)
minute.color("yellow")
minute.shapesize(stretch_wid=0.2, stretch_len=13)


#the second pointer
second = turtle.Turtle()
second.shape("arrow")
second.speed(50)
second.color("red")
second.shapesize(stretch_wid=0.1,stretch_len=18)


#the mini circle
mini=turtle.Turtle()
mini.speed(50)
mini.hideturtle()
mini.penup()
mini.goto(0,-5)
mini.hideturtle()
mini.pendown()
mini.fillcolor("brown")
mini.begin_fill()
mini.circle(5)
mini.end_fill()

animation.ontimer(revolution_of_hour,1)
animation.ontimer(revolution_of_minute,1)
animation.ontimer(revolution_of_second,1)
animation.exitonclick()
turtle.done()