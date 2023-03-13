import tkinter
from timer_mechanism import TimerMechanism
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
timer_mechanism = TimerMechanism()


def start_clicked():
	print("start clicked")
	if timer_mechanism.state == "off":
		timer_mechanism.state = "working"
		main_label.config(text="Work", fg=RED)
		count_down(WORK_MIN * 60)


def reset_clicked():
	timer_mechanism.reset_mechanism()
	main_label.config(text="Timer", fg=GREEN)
	checkmark_label.config(text=timer_mechanism.text_of_checkmarks)


def state_changer():
	new_state = timer_mechanism.change_state()
	match new_state:
		case "working":
			count_down(WORK_MIN*60)
			main_label.config(text="Work", fg=RED)
		case "resting":
			count_down(SHORT_BREAK_MIN*60)
			main_label.config(text="Rest", fg=GREEN)
		case "long resting":
			count_down(LONG_BREAK_MIN*60)
			main_label.config(text="Long Rest", fg=GREEN)
		case _:
			print("it is off")

	checkmark_label.config(text=timer_mechanism.text_of_checkmarks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
	if timer_mechanism.state != "off":
		minutes = str(int(count/60))
		seconds = str(int(count % 60))
		if len(minutes) == 1:
			minutes = "0" + minutes
		if len(seconds) == 1:
			seconds = "0" + seconds
		time_amount = minutes + ":" + seconds
		canvas.itemconfig(timer_text, text=time_amount)
		if count > 0:
			window.after(1000, count_down, count-1)
		else:
			state_changer()
	else:
		canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Pomodoro countdown")
window.config(padx=110, pady=50, bg=YELLOW)

fg = GREEN
main_label = tkinter.Label(text="Timer", font=(FONT_NAME, 28, "bold"), foreground=fg, bg=YELLOW)
main_label.config(padx=20, pady=20, width=10)
main_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

# count_down(15)

start_button = tkinter.Button(text="start", command=start_clicked, bg=GREEN, foreground="white", font=(FONT_NAME, 14, "bold"))
start_button.config(padx=5, pady=2)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(text="reset", command=reset_clicked, bg=GREEN, foreground="white", font=(FONT_NAME, 14, "bold"))
reset_button.config(padx=5, pady=2)
reset_button.grid(column=2, row=2)


checkmark_label = tkinter.Label(text="", font=(FONT_NAME, 20, "bold"), foreground=fg, bg=YELLOW)
checkmark_label.config(padx=0, pady=10)
checkmark_label.grid(column=1, row=3)

window.mainloop()
