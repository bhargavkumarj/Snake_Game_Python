from turtle import Screen,Turtle
import time
from scoreboard import ScoreBoard
from snake import Snake
from food import Food
screen=Screen()
screen.bgcolor("black")
screen.title("Bhargav's_snake_game")
screen.setup(605,605)
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=ScoreBoard()
border=Turtle()
border.color('white')
border.hideturtle()
border.penup()
border.forward(300)
border.pendown()
border.left(90)
border.forward(300)
for i in range (3):
    border.left(90)
    border.forward(600)
border.left(90)
border.forward(300)




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    """"Detect collision with food"""
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #print("nom nom nom")
    """Detect collision with wall"""
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        game_is_on=False
        scoreboard.game_over()
    """"Detect collision with tail"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:

            scoreboard.game_over()
screen.exitonclick()