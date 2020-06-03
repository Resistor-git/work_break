# TODO
# user input (interface)
# add a timer window
# align window (lower center?)
# ? refactor into several files: logic, interface ...
# ? refactor to classes (mostly tkinter)

# окно с перезапуском не пропадает после нажатия кнопки
# для рефакторинга может пригодиться tk.toplevel

#import datetime as dt
import time
import tkinter as tk


def user_input():
    """Gets the data from user_input and uses it to launch countdown"""
    global h, m, s
    h = hours.get()
    m = minutes.get()
    s = seconds.get()
    #print(h,m,s)
    user_inp.destroy()
    # countdown(int(h), int(m), int(s))


def countdown(hours=0, mins=0, secs=30):
    countdown_secs = (hours * 3600) + (mins * 60) + secs
    while countdown_secs > 0:
        print('start', countdown_secs)
        time.sleep(1)
        countdown_secs -= 1
        print('finish', countdown_secs)


def user_inp_window():
    # window prompting user to enter hours, minutes and seconds
    global user_inp, hours, minutes, seconds

    user_inp = tk.Tk()
    user_inp.title("Введите данные о перерыве")

    hours = tk.Entry(user_inp)
    hours.insert(0, "0")
    hours.pack()
    hours.focus_set()
    minutes = tk.Entry(user_inp)
    minutes.insert(0, "0")
    minutes.pack()
    seconds = tk.Entry(user_inp)
    seconds.insert(0, "2")
    seconds.pack()

    ok_button = tk.Button(user_inp, text='OK', command=user_input)
    ok_button.pack(side='bottom')

    user_inp.mainloop()


# def timer_window():
#     timer = tk.Tk()
#     timer.title('До следующего перерыва осталось:')
#
#     hours_left = hours
#     minutes_left = minutes
#     seconds_left = seconds
#
#     initial_time = dt.time(hours_left, minutes_left, seconds_left)
#     time_left =


def break_msg_window():
    # widget informs about the break time and asks for restart
    break_msg = tk.Tk()
    break_msg.title('Сообщение о перерыве')

    #frame = tk.Frame(root)
    #frame.pack()

    break_msg_text = tk.Label(text='Пора на перерыв', font='arial 32')
    break_msg_text.pack()

    # the following string doesn't work as intended if 'command=countdown(int(h), int(m), int(s)))'
    # google: 'tkinter button executed automatically'. Answer: either use lambda, or use functools.partial
    reset_button = tk.Button(break_msg, text='Перезапустить таймер c прежними параметрами',
                             command=(lambda: countdown(int(h), int(m), int(s))))
    reset_button.pack()

    break_msg.mainloop()


def runner():
    user_inp_window()
    countdown(int(h), int(m), int(s))
    break_msg_window()



runner()
