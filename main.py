# todo make second part of the snake game

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game!")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.add_tail()
        scoreboard.increase_score()

    if -290 > snake.head.xcor() or snake.head.xcor() > 290 or -290 > snake.head.ycor() or snake.head.ycor() > 290:
        game_is_on = False
        scoreboard.game_over()

    for snake_part in snake.snakes[1:]:
        if snake.head.distance(snake_part) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
