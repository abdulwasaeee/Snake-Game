import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)


    def refresh(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))
