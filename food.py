from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("green")
        self.speed(9 )
        self.refresh_food()


    def refresh_food(self):
        random_x = random.randint(-280, 280)  # we don't want food to be at the wall
        random_y = random.randint(-280, 280)  # because our snake dies as soon as reaches the wall
        self.goto(random_x, random_y)