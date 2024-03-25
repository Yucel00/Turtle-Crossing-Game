from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.left(90)

    def up(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def level_up_control(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False
