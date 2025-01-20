from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake(Turtle):
    def __init__(self):
     super().__init__()
     self.segments=[]
     self.create()
     self.head=self.segments[0]

    def create(self):
         for i in STARTING_POSITIONS:
             self.add_segment(i)

    def add_segment(self,position):
         t=Turtle()
         t.penup()
         t.shape("square")
         t.color("white")
         t.goto(position)
         self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            newx=self.segments[i-1].xcor()
            newy=self.segments[i-1].ycor()
            self.segments[i].goto(newx,newy)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
         self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)

