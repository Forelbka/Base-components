import tkinter as tk

operatins = ['+', '-', '/', '^']
window = tk.Tk()
label = tk.Label(text="Формула")
entr = tk.Entry()
entr.pack()
label.pack()

from turtle import *

y = min(screensize())
y = 500

class Function():
    def __init__(self, string):
        self.string = string
        self.a = 0
        self.step = 0
        self.b = 0
        self.c = 0
        self.generate_func()

    def generate_func(self):
        strin = self.string.split()
        a = 1
        step = 1
        if len(strin) == 5:
            if strin[0][:strin[0].find('x')]:
                a = float(strin[0][:strin[0].find('x')])
            step = float(strin[0][strin[0].find('^') + 1:])
            b = float(strin[1] + strin[2][:-1])
            c = float(strin[3] + strin[4])
        else:
            if strin[0][:strin[0].find('x')]:
                b = float(strin[0][:strin[0].find('x')])
            else:
                b = 1
            c = float(strin[1] + strin[2])
            a = 0
        self.a = a
        self.step = step
        self.b = b
        self.c = c

    def get_func(self, x):
        return (self.a * (x ** self.step)) + (self.b * x) + self.c
    
    def print_func(self, start=y * -1, finish=y):
        clear()
        speed(10000)
        pensize(2)
        step = (y * 2) // 10
        pu()
        setpos(0, 0)
        pd()
        goto(y * -1, 0)
        for _ in range(9):
            goto(xcor() + step, 0)
            goto(xcor(), 10)
            goto(xcor(), -10)
            goto(xcor(), 0)
        goto(y, 0)
        goto(0, 0)
        goto(0, y)
        goto(0, y * -1)
        for _ in range(9):
            goto(0, ycor() + step)
            goto(10, ycor())
            goto(-10, ycor())
            goto(0, ycor())
        pu()
        setpos(start, y // 2)
        results = [self.get_func(i / step) for i in range(((finish - start) // 2) * -1, (finish - start) // 2)]
        goto(y * -1, results[0] * step)
        pd()
        for i in range(finish - start - 1):
            goto(i - y, int(results[i] * step))
        #mainloop()


def handle_keypress(event):
    f = Function(entr.get())
    f.print_func()

window.bind("<Return>", handle_keypress)

window.mainloop()