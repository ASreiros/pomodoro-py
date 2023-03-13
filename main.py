import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# ---------------------------- UI SETUP ------------------------------- #


def start_clicked():
	print("start clicked")


def reset_clicked():
	print("reset clicked")


window = tkinter.Tk()
window.title("Pomodoro countdown")
window.config(padx=110, pady=50, bg=YELLOW)

fg = GREEN
state_text = "Work Timer"
main_label = tkinter.Label(text=state_text, font=(FONT_NAME, 28, "bold"), foreground=fg, bg=YELLOW)
main_label.config(padx=20, pady=20)
main_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")

timer = "00:00"
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text=timer, fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="start", command=start_clicked, bg=GREEN, foreground="white", font=(FONT_NAME, 14, "bold"))
start_button.config(padx=5, pady=2)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="reset", command=reset_clicked, bg=GREEN, foreground="white", font=(FONT_NAME, 14, "bold"))
reset_button.config(padx=5, pady=2)
reset_button.grid(column=2, row=2)

checkmark = "✔"
checkmark_text = checkmark

checkmark_label = tkinter.Label(text=checkmark_text, font=(FONT_NAME, 20, "bold"), foreground=fg, bg=YELLOW)
checkmark_label.config(padx=0, pady=10)
checkmark_label.grid(column=1, row=3)



window.mainloop()