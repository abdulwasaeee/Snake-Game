from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score=0
        self.goto(0,270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", False, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center")

    def increase_score(self):
        self.score+=1
        self.update_score()


