from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x= -40, y=280)
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"score = {self.score}", move=False, align='left', font=('Courier', 13, 'normal'))

    def game_over(self):
        self.color("red")
        self.goto(-40, 0)
        self.write(arg="Game over", move=False, align='left', font=('Courier', 20, 'normal'))



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
