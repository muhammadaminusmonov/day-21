from turtle import Turtle

SNAKE_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for snake_position in SNAKE_POSITION:
            self.add_snake(snake_position)

    def add_snake(self, position):
        new_snake = Turtle(shape="square")
        new_snake.up()
        new_snake.color("white")
        new_snake.goto(position)
        self.snakes.append(new_snake)

    def add_tail(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for i in range(len(self.snakes)-1, 0, -1):
            x_position = self.snakes[i - 1].xcor()
            y_position = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x_position, y_position)
        self.head.forward(20)

    def up(self):
        current_direction = self.head.heading()
        if current_direction != 270:
            self.head.setheading(90)

    def down(self):
        current_direction = self.head.heading()
        if current_direction != 90:
            self.head.setheading(270)

    def left(self):
        current_direction = self.head.heading()
        if current_direction != 0:
            self.head.setheading(180)

    def right(self):
        current_direction = self.head.heading()
        if current_direction != 180:
            self.head.setheading(0)
