from re import A, S
from tkinter import W
import turtle

#display:
#screen, dimensions, color, title
sc= turtle.Screen()
sc.setup(600, 400)
sc.bgcolor("black")
sc.title("Pong")

#leftpaddle:
#turtle, speed, shape, color, position
lpaddle= turtle.Turtle()
lpaddle.speed(0)
lpaddle.color("white")
lpaddle.shape("square")
lpaddle.shapesize(3,0.5)
lpaddle.penup()
lpaddle.setpos(-275,0)


#rightpaddle
#turtle, speed, shape, color, positon
rpaddle= turtle.Turtle()
rpaddle.speed(0)
rpaddle.color("white")
rpaddle.shape("square")
rpaddle.shapesize(3,0.5)
rpaddle.penup()
rpaddle.setpos(275,0)

#ball
#turtle, speed, shape, color, position
ball= turtle.Turtle()
ball.speed(40)
ball.color("white")
ball.shape("circle")
ball.shapesize(0.5, 0.5)
ball.penup()
ball.x= 5
ball.y= 5

#score_variables
lscore= 0
rscore= 0 

#score_display
score=turtle.Turtle()
score.hideturtle()
score.penup()
score.color("white")
score.setpos(0,180)
score.pendown()
score.write("Player 1: {}   Player 2: {}".format(lscore, rscore), align= "center", font= ("Courier", "14"))

#lpadup
def lpadup() :
    y= lpaddle.ycor()
    y+= 20
    lpaddle.sety(y)

#lpaddown
def lpaddown() :
    y= lpaddle.ycor()
    y-= 20
    lpaddle.sety(y)

#rpadup
def rpadup() :
    y= rpaddle.ycor()
    y+= 20
    rpaddle.sety(y)

#rpaddown
def rpaddown() : 
    y= rpaddle.ycor()
    y-= 20
    rpaddle.sety(y)

#keybinds
sc.listen()
sc.onkeypress(lpadup, "w")
sc.onkeypress(lpaddown, "s")
sc.onkeypress(rpadup, "Up")
sc.onkeypress(rpaddown, "Down")


while True:
    sc.update()
    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor()+ ball.y)

    #parametros_y
    if ball.ycor() > 200 :
        ball.y *= -1

    if ball.ycor() < -200 : 
        ball.y *= -1
    
    #parametros_x
    if ball.xcor() > 300 :
        sc.delay(15)
        ball.setpos(0, 0)
        ball.x *= -1
        lscore += 1
        score.clear()
        score.write("Player 1: {}   Player 2: {}".format(lscore, rscore), align= "center", font= ("Courier", "14"))

    if ball.xcor() < -300 :
        sc.delay(15)
        ball.setpos(0,0)
        ball.x *= -1
        rscore += 1
        score.clear()
        score.write("Player 1: {}   Player 2: {}".format(lscore, rscore), align= "center", font= ("Courier", "14"))
    
    #collision
    
    if (ball.xcor()>275) and (ball.xcor()<285) and (ball.ycor()<rpaddle.ycor()+20 and ball.ycor()>rpaddle.ycor()-20) :
        ball.x *= -1

    if (ball.xcor()<-275) and (ball.xcor()>-290) and (ball.ycor()<lpaddle.ycor()+40 and ball.ycor()>lpaddle.ycor()-40) :
        ball.setx(-275)
        ball.x *= -1


    