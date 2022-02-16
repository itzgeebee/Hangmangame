# import the needed classes
import turtle
from state_print import StatePrint

screen = turtle.Screen()
screen.title("US states")
image = ("us-states-game-start/blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)
state_p = StatePrint()

# condition for running program
while state_p.answered < 50:

    answer = screen.textinput(title= f"US states: {state_p.answered} / {state_p.total}", prompt="Name a state").title()
    if answer == "Exit":
        state_p.game_over()
        break

    state_p.show_state(answer)
screen.exitonclick()



