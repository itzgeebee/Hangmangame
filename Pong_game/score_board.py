# The scoreboard class which defines the attributes and methods of the scoreboard
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.speed("fastest")
        self.update_score()


    def update_score(self):
        """ updates the score board"""
        self.goto(-200, 230)
        self.write(arg=self.left_score, move=False, align='left', font=('Courier', 50, 'normal'))
        self.goto(180, 230)
        self.write(arg=self.right_score, move=False, align='left', font=('Courier', 50, 'normal'))

    def increase_lscore(self):
        """ increases the left score by 1 """
        self.left_score += 1
        self.clear()
        self.update_score()

    def increase_rscore(self):
        """ increases the right score by 1 """
        self.right_score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        """prints out the final messages when game termination condition is met"""
        self.goto(-150, 0)
        self.write(arg="Game Over", move=False, align='left', font=('Courier', 50, 'normal'))
        if self.left_score > self.right_score:
            self.goto(-250, 150)
            self.write(arg="left side wins", move=False, align='left', font=('Courier', 50, 'normal'))
        else:
            self.goto(-250, 150)
            self.write(arg="Right side wins", move=False, align='left', font=('Courier', 50, 'normal'))




