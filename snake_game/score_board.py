from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # get the high_score data from a .txt file
        with open("snake_game\data.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())
        self.ht()
        self.penup()
        self.color("white")
        self.goto(x= -40, y=280)
        self.speed("fastest")
        self.update_scoreboard()


    def update_scoreboard(self):
        """clears the previous score from the screen and updates the new score"""
        self.clear()
        self.write(arg=f"score = {self.score} High score = {self.high_score}", move=False, align='left', font=('Courier', 13, 'normal'))

    def reset(self):
        """overwrites the previous high_score if it is less than the score when the user starts again"""
        if self.score > (self.high_score):
            self.high_score = self.score
        # writes the new high_score in the .txt file
        with open("data.txt", mode="w") as high_score:
            high_score.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """increases the score by 1 and calls the update scoreboard function"""
        self.score += 1
        self.update_scoreboard()
