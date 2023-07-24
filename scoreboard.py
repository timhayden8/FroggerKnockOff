from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-180,260)
        self.score=0
        self.write(f"Score:{self.score}",font = FONT)
    
    def increasescore(self):
        self.score +=1
        self.clear()
        self.write(f"Score:{self.score}",font = FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",font = FONT)
