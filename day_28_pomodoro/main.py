import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global paused
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    start_button.config(text="Start", command=start_timer)
    paused = False


# ---------------------------- TIMER MECHANISM ------------------------------- #


paused = False


def convert_string(paused_string):
    paused_split = paused_string.split(":")
    minutes_sec = (int((paused_split[0])) * 60) + int(paused_split[1])
    return minutes_sec


def pause():
    global paused
    window.after_cancel(timer)
    start_button.config(text="Start", command=start_timer)
    paused = True


def start_timer():
    global reps
    global paused
    if not paused:
        start_button.config(text="Pause", command=pause)
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if not reps % 8:
            # long break
            count_down(long_break_sec)
            title_label.config(text="Break", fg=RED)
        elif reps % 2:
            # work
            count_down(work_sec)
            title_label.config(text="Work", fg=GREEN)
        else:
            # short break
            count_down(short_break_sec)
            title_label.config(text="Break", fg=PINK)
    elif paused:
        paused_string = canvas.itemcget(timer_text, "text")
        paused_seconds = convert_string(paused_string)
        count_down(paused_seconds)
        start_button.config(text="Pause", command=pause)
        paused = False


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if not reps % 2:
            marks = ""
            for _ in range(reps // 2):
                marks += "✔"
                check_marks.config(text=marks)

        # Brings the app to the front
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(
    103, 122, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# title label
title_label = tk.Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

# buttons
start_button = tk.Button(
    text="Start", bg="white", fg="black", highlightthickness=0, command=start_timer
)
start_button.grid(column=0, row=2)
reset_button = tk.Button(
    text="Reset", bg="white", fg="black", highlightthickness=0, command=reset_timer
)
reset_button.grid(column=2, row=2)

check_marks = tk.Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
window.mainloop()
