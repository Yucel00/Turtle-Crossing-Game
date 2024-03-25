from turtle import Turtle
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()

        self.level=0
        self.update_score()


    def update_score(self):
        self.goto(-260,260)
        self.write(f"LEVEL{self.level}",align="center",font=FONT)



    def level_score(self):
        self.level+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
