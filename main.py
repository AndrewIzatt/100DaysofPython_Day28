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
LONG_BREAK_MIN = 10
REPS = 0
CHECKMARK_CHAIN = []
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    REPS += 1
    if REPS % 2 == 0:
        CHECKMARK_CHAIN.append("✓")
        check_label.config(text="".join(CHECKMARK_CHAIN))
    if REPS % 8 == 0:
        main_label.config(text=f"Break", fg=PINK)
        countdown(long_break_sec)
    elif REPS % 2 != 0:
        main_label.config(text=f"Work", fg=GREEN)
        countdown(work_sec)
    else:
        main_label.config(text=f"Break", fg=RED)
        countdown(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # window.after(ms=1000, func=countdown, count - 1)
        window.after( 1000, countdown, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

main_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
main_label.grid(row=0, column=1)
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()