from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = 0

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global timer
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    ticks_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    if not timer:
        reps += 1
        work_sec = int(WORK_MIN * 60)
        sb_sec = int(SHORT_BREAK_MIN * 60)
        lb_sec = int(LONG_BREAK_MIN * 60)
        if reps % 8 == 0:
            timer_label.config(text="Break", fg=RED)
            countdown(lb_sec)
        elif reps % 2 == 0:
            timer_label.config(text="Break", fg=PINK)
            countdown(sb_sec)
        else:
            timer_label.config(text="Work", fg=GREEN)
            countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        timer = None
        start_timer()
        mark = ""
        for i in range(math.floor(reps/2)):
            mark = mark + "🗸"
        ticks_label.config(text=mark)

# ---------------------------- Pause Mechanism ------------------------------- #


def pause_timer():
    global timer, paused
    if paused:
        pause_button.config(text="Pause")
        time_left = canvas.itemcget(timer_text, "text").split(":")
        count = int(time_left[0]) * 60 + int(time_left[1])
        countdown(count)
        paused = 0
    else:
        pause_button.config(text="Unpause")
        window.after_cancel(timer)
        paused = 1

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=3)

ticks_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
ticks_label.grid(column=1, row=2)

pause_button = Button(text="Pause", command=pause_timer)
pause_button.grid(column=1, row=3)


window.mainloop()
