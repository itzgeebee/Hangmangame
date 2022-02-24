import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 40
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
time_loop = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(time_loop)
    canvas.itemconfig(timer_text, text= "00:00")
    check_marks.config(text="")
    timer.config(text="Timer", fg=GREEN)
    global reps
    reps = 0




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60
    global reps
    reps +=1
    if reps % 8 == 0:
        count_down(long_sec)
        timer.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short_sec)
        timer.config(text="Short Break", fg= PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work Session", fg= RED )








# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg = YELLOW)





canvas = Canvas(width=200, height=224, bg = YELLOW, highlightthickness= 0)
photo = PhotoImage(file ="pomodoro/tomato.png")
canvas.create_image(100, 112, image = photo, )
timer_text = canvas.create_text(100, 130, text="00:00", fill =("white"), font=(FONT_NAME, 35, "bold"), )
canvas.grid(column=1, row=1)

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    count_timer = f"{count_min}:{count_sec}"


# ---------------------------- TIMER MECHANISM ------------------------------- # 
    canvas.itemconfig(timer_text, text= count_timer)
    if count > 0:
        global time_loop
        time_loop = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_session = math.floor(reps/2)
        marks = ""
        for i in range(work_session):
            marks += "✔"
            check_marks.config(text=marks)




timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg= GREEN, bg= YELLOW, highlightthickness= 0)
timer.grid(column=1, row = 0)

reset = Button(text="Reset", font=(FONT_NAME, 15, "bold"), fg= "black", bg= "white", command=reset_timer)
reset.grid(column=2, row=2)

start = Button(text="Start", font=(FONT_NAME, 15, "bold"), fg= "black", bg= "white", command=start_timer)
start.grid(column=0, row=2)

check_marks = Label(font=(FONT_NAME, 12, "bold"), fg="black", bg=YELLOW)
check_marks.grid(column=1, row=3)





window.mainloop()