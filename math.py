from symbol import del_stmt
import tkinter as tk
from turtle import *

y = min(screensize())
#y = 500

#operatins = ['+', '-', '/', '^']
label = tk.Label(text="Формула")
entr = tk.Entry()
button = tk.Button(text="Нарисовать")
entr.pack()
label.pack()
button.pack()

class Function():
    def __init__(self, string):
        self.string = string
        self.a = 0
        self.step = 0
        self.b = 0
        self.c = 0

    def get_func(self, x):
        strin = self.string.split()
        gl_rez = 0
        l_rez = 1
        znak = True
        for el in strin:
            l_rez = 1
            if len(el) > 1 or el == 'x' or el in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if not znak:
                    l_rez *= -1
                    znak = True
                if 'x' in el:
                    if not '^' in el:
                        l_rez *= x
                    el = el.split('x')
                    if el[0]:
                        if el[0] == '-':
                            l_rez *= -1
                        else:
                            l_rez *= float(el[0])
                    if el[1]:
                        l_rez *= x ** float(el[1][1:])
                else:
                    l_rez *= float(el)
                gl_rez += l_rez
            else:
                if el == '-':
                    znak = False
        return gl_rez


    def print_func(self, start=(y * -1), finish=y):
        if '^0.' in self.string and start < 0:
            start = 0
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
        results = [self.get_func(i / step) for i in range(start, finish)]
        goto(start, results[0] * step)
        pd()
        for i in range(start, finish):
            goto(i, int(results[i - start] * step))


def handle_keypress(event):
    f = Function(entr.get())
    f.print_func()


button.bind("<Button-1>", handle_keypress)
mainloop()