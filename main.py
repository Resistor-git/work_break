# TODO
# countdown
# text window
# user input (console)
# user input (interface)
# align window (lower center?)
# ? refactor into several files: logic, interface ...
# ? refactor to classes (mostly tkinter)

# прога просит ввести время, начинает отсчёт и окно закрывается
# таймер доходит до нуля и появляется окно с предложением перезапуска
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
    countdown(int(h), int(m), int(s))


def countdown(hours=0, mins=0, secs=30):
    print('h=', hours)
    countdown_secs = (hours * 3600) + (mins * 60) + secs
    while countdown_secs > 0:
        time.sleep(1)
        countdown_secs -= 1
        print(countdown_secs)


#def restarter():
 #   countdown(h, m, s)

# widget prompting user to enter hours, minutes and seconds
user_inp=tk.Tk()
user_inp.title("Введите данные о перерыве")

hours = tk.Entry(user_inp)
hours.pack()
hours.focus_set()
minutes = tk.Entry(user_inp)
minutes.pack()
seconds = tk.Entry(user_inp)
seconds.pack()

ok_button = tk.Button(user_inp, text='OK', command=user_input)
ok_button.pack(side='bottom')

user_inp.mainloop()


# widget informing about the break time and asks for restart
break_msg = tk.Tk()
break_msg.title('Сообщение о перерыве')

#frame = tk.Frame(root)
#frame.pack()

break_msg_text = tk.Label(text='Пора на перерыв', font='arial 32')
break_msg_text.pack()

reset_button = tk.Button(break_msg, text='Перезапустить таймер', command=countdown(int(h), int(m), int(s)))
#reset_button = tk.Button(frame, text='Перезапустить таймер', command=countdown(0, 0, 3))
reset_button.pack()

break_msg.mainloop()



#def runner():
#    print(countdown_time)
#    countdown(countdown_time)

#user_input()