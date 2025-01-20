import time
from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.title("snake-game")
screen.tracer(0)
screen.setup(height=600,width=600)
screen.listen()
screen.bgcolor("black")
snake=Snake()
food=Food()
score=Score()
game=True
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.refresh()
        score.clear()
        score.increase_score()
        snake.extend()
    if snake.head.xcor()> 290 or snake.head.xcor()< -290 or snake.head.ycor()> 290 or snake.head.ycor()< -290:
        game=False
        score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game=False
            score.game_over()

screen.exitonclick()
