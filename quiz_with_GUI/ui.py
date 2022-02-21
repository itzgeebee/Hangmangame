THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx= 20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0,row=1, columnspan=2,pady= 50)
        self.question_text = self.canvas.create_text(150,100, text= "Text", fill="black", font=("Arial",15,"italic"), width= 280 )
        x_image =PhotoImage(file="quiz_with_GUI/images/false.png")
        check_image = PhotoImage(file="quiz_with_GUI/images/true.png")
        self.check_button = Button(image=check_image, highlightthickness=0, command= self.green_button)
        self.check_button.grid(column=0, row =2)
        self.x_button = Button(image=x_image, highlightthickness=0, command=self.red_button)
        self.x_button.grid(column=1, row=2)
        self.label = Label(text=f"score: ", font=("Arial", 12, "bold"), fg="white", bg=THEME_COLOR )
        self.label.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        """Generates the next question form the list of questions"""
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"score: {self.quiz.score} ")
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question_text, text=f"End of quiz. final score: "
                                                            f"{self.quiz.score}/{self.quiz.question_number}")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")


    def green_button(self):
        """checks if the answer to a question is correct"""
        is_right= self.quiz.check_answer("True")
        self.feedback(is_right)
    def red_button(self):
        """checks if the answer to a question s correct"""
        is_right= self.quiz.check_answer("False")
        self.feedback(is_right)


    def feedback(self, is_right):
        """ changes the canvas color based on button responses"""
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        # calls next question after 1 second
        self.window.after(1000, self.get_next_question)


