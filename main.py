# TODO
# countdown
# text window
# user input (console)
# user input (interface)
# align window (lower center?)
# ? refactor into several files: logic, interface ...
# ? refactor to classes (mostly tkinter)

#import datetime as dt
import time
import tkinter as tk


def countdown(hours=0, mins=0, secs=0):
    countdown_secs = (hours * 3600) + (mins * 60) + secs
    while countdown_secs > 0:
        time.sleep(1)
        countdown_secs -= 1
        print(countdown_secs)
    break_window()


def break_window():
    root = tk.Tk()
    #   fr = tk.Frame(root)
    root.title('Сообщение о перерыве')
    message = tk.Label(text='Пора на перерыв', font='arial 32')
    message.pack()
    root.mainloop()


def user_input():
    pass


countdown(secs=5)

