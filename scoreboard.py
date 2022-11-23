from turtle import  Turtle
ALIGNMENT="center"
FONT=("Arial", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("highscore.txt") as high_score:
            self.highscore=int(high_score.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} ,High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("highscore.txt",mode="w") as high_score:
                high_score.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score+=1

        self.update_scoreboard()
