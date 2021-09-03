from tkinter import *
import time
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
check_count = ''
timer = None

#resets the timer
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='0:00')
    global check_count

    timer_label.config(text='タイマー', fg=GREEN)
    check_count = ''
    check_mark.config(text=check_count)


#timer mechanism
def start_timer():
    global reps
    global check_count
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="長い休憩", fg=RED)
        count_down(1200)
    elif reps % 2 == 0:
        timer_label.config(text="休憩", fg=PINK)
        check_count += "✔"
        check_mark.config(text=check_count)
        count_down(300)
    else:
        timer_label.config(text="仕事中", fg=GREEN)
        count_down(1500)
    
    
    
        

#countdown mechanism
def count_down(count):
    global timer
    seconds = count % 60
    minutes = math.floor((count / 60))
    if seconds < 10:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
#window creation
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)


#Canvas creation
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#canvas w/image
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
canvas.grid(column=1, row=1)

#canvas w/text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
#timer function


#'Timer' label
timer_label = Label(text='タイマー', font=(FONT_NAME, 50))
timer_label.config(fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)




#Start and reset buttons
start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)
start_button.config(bg='white')

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)
reset_button.config(bg='white')

#check mark
check_mark = Label(text=check_count, font=(FONT_NAME, 15, 'bold'))
check_mark.config(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

#loop runs
window.mainloop()