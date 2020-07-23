# TODO
# user input interface improvements (names for entries :'часы, минуты, секунды')
# StringVar() https://metanit.com/python/tutorial/9.6.php
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
        print('countdown finished')


def user_inp_window():
    # window prompting user to enter hours, minutes and seconds
    global user_inp, hours, minutes, seconds

    user_inp = tk.Tk()
    user_inp.title("Введите данные о перерыве")

    user_inp.geometry('350x100')

    hours = tk.Entry(user_inp)
    hours.insert(0, "0")
    hours.pack()
    hours.focus_set()  # sets cursor on this place
    minutes = tk.Entry(user_inp)
    minutes.insert(0, "0")
    minutes.pack()
    seconds = tk.Entry(user_inp)
    seconds.insert(0, "2")
    seconds.pack()

    ok_button = tk.Button(user_inp, text='OK', command=user_input)
    ok_button.pack(side='bottom')

    user_inp.mainloop()
    print('user_inp_window finished')


def break_msg_window():
    # widget informs about the break time and asks for restart
    global break_msg

    break_msg = tk.Tk()
    break_msg.title('Сообщение о перерыве')
    break_msg.attributes("-topmost", True)  # places this widget on top of all other windows

    break_msg_text = tk.Label(text='Пора на перерыв', font='arial 32')
    break_msg_text.pack()

    # creation of the reset button
    # the following string doesn't work as intended if 'command=reset()'
    # google: 'tkinter button executed automatically'. Answer: either use lambda, or use functools.partial
    reset_button = tk.Button(break_msg, text='Перезапустить таймер c прежними параметрами', command=(lambda: reset()))
    reset_button.pack()


    break_msg.mainloop()
    print('break_msg_window finished')


def reset():
    # reset button ('Перезапустить таймер с прежними параметрами') functionality
    break_msg.destroy()
    countdown(int(h), int(m), int(s))
    break_msg_window()
    print('reset finished')


def runner():
    user_inp_window()
    countdown(int(h), int(m), int(s))
    break_msg_window()


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


runner()
