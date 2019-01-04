#Screen creation using turtle
import turtle
import winsound

score_a=0
score_b=0
wn = turtle.Screen()
wn.title("Ping Pong by @yash and @pramay")
wn.bgcolor("purple")
wn.setup(width=1024,height=768)
wn.tracer(0)


#Score

pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.write("Player A:0	Player B:0",align="center",font=("Courier",24,"bold"))


#Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-470,0)

#Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(460,0)

#Function
def paddle_a_up():
	y=paddle_a.ycor()
	y+=20
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y-=20
	paddle_a.sety(y)

def paddle_b_up():
	y=paddle_b.ycor()
	y+=20
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y-=20
	paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Ball
ball = turtle.Turtle()
ball.speed(50)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.35
ball.dy=-0.35


#Main Loop
while True:
	wn.update()
	# winsound.PlaySound("back.wav",winsound.SND_ASYNC)
	ball.sety(ball.ycor()+ball.dy)
	ball.setx(ball.xcor()+ball.dx)

	if ball.ycor() > 374:
		ball.sety(374)
		ball.dy*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

	if ball.ycor() < -374:
		ball.sety(-374)
		ball.dy*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

	if ball.xcor() > 502:
		ball.goto(0,0)
		ball.dx*=-1
		score_a+=1
		pen.clear()
		pen.write("Player A:{}	Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"bold"))

	if ball.xcor() < -502:
		ball.goto(0,0)
		ball.dx*=-1
		score_b+=1
		pen.clear()
		pen.write("Player A:{}	Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"bold"))


    #Paddle collision with ball

	if (ball.xcor()>450 and ball.xcor()<470) and (ball.ycor() < (paddle_b.ycor()+50) and ball.ycor() > (paddle_b.ycor()-50)):
		ball.setx(450)
		ball.dx*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

	if (ball.xcor()<-450 and ball.xcor()>-470) and (ball.ycor() < (paddle_a.ycor()+50) and ball.ycor() > (paddle_a.ycor()-50)):
		ball.setx(-450)
		ball.dx*=-1
		winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)