# import turtle for the GUI and pandas to access the csv
from turtle import Turtle
import pandas as pd

states = pd.read_csv("us-states-game-start/50_states.csv")


class StatePrint(Turtle):

    def __init__(self):
        """initializes the State attribute"""
        super().__init__()

        self.ht()
        self.penup()
        self.state_list = (states.state.to_list())
        self.x_coord = states.x.to_list()
        self.y_coord = states.y.to_list()
        self.answered = 0
        self.total = len(states)
        self.missing_states = []
        self.color("black")
        self.answer_list = []


    def show_state(self, ans):
        """takes in one argument and checks if it is equal to one of the elements in state list and writes that
        element on the specified position on the screen """
        for i in range(len(self.state_list)):

            if ans == self.state_list[i] and ans not in self.answer_list:
                x = float(self.x_coord[i])
                y = float(self.y_coord[i])
                self.goto(x, y)
                self.write(arg=f"{self.state_list[i]}")
                self.answered += 1
                self.answer_list.append(ans)

    def game_over(self):
        """writes game over message. compares the amount of correctly guessed states with the state list and writes
        the incorrectly guessed on the screen. Also adds the incorrect states to a csv file """
        self.color("blue")
        self.goto(-220, 250)
        self.write(arg=f"Game over. You got {self.answered}/{self.total} states", font=('Courier', 20, 'normal'))
        for i in range(len(self.state_list)):
            if self.state_list[i] not in self.answer_list:
                self.color("red")
                self.speed("fastest")
                self.goto(float(self.x_coord[i]), float(self.y_coord[i]))
                self.write(arg=f"{self.state_list[i]}")
                self.missing_states.append(self.state_list[i])
                df = pd.DataFrame(self.missing_states)
        missed_states = df.to_csv("missedstates.csv")









