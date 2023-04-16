from turtle import Turtle
ALIGN='center'
FONT=('Courier',24,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.write(f"Score:{self.score}  High Score:{self.highscore}",align=ALIGN,font=FONT)
        self.hideturtle()
        #self.goto(0,270)
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}", align=ALIGN, font=FONT)
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
    # def game_over(self):
    #     self.goto(0,0)

        self.write("GAME OVER", align=ALIGN, font=FONT)
        #self.goto(0,0)




    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()