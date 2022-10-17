from re import S
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

def get_f(strin, x):
    strin = strin[:]
    l_rez = 1
    if 'x' in strin:
        if not '^' in strin:
            l_rez *= x
        strin = strin.split('x')
        if strin[0]:
            if strin[0] == '-':
                l_rez *= -1
            else:
                l_rez *= float(strin[0])
        if strin[1]:
            l_rez *= x ** float(strin[1][1:])
    else:
        l_rez *= float(strin)
    return l_rez

class Function():
    def __init__(self, string):
        self.string = string
        self.a = 0
        self.step = 0
        self.b = 0
        self.c = 0

    def get_func(self, x):
        strin = self.string
        znak = 1
        summ = 0
        l_sum = 1
        if '(' in strin or ')' in strin:
                    count_s = 0
                    ind_f = 0
                    if strin[0] != '(':
                        l_sum *= get_f(strin[:strin.find('(')], x)
                        ind_f = strin.find('(')
                    for n, zn in enumerate(strin[ind_f:]):
                        if zn == '(':
                            count_s += 1
                        elif zn == ')':
                            count_s -= 1
                        if count_s == 0:
                            ferst_f = Function(strin[ind_f + 1:n])
                            sec_f = Function(strin[n + 1:])
                            if n != len(strin) and strin[n + 1:]:
                                summ += ferst_f.get_func(x) + sec_f.get_func(x) * l_sum
                            else:
                                summ += ferst_f.get_func(x)
                            break
        else:
            strin = strin.split()
            for el in strin:
                if len(el) > 1 or el == 'x' or el in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    if '/' in el:
                        n = el.find('/')
                        if get_f(el[n + 1:], x) == 0:
                            return None
                        else:
                            summ += (get_f(el[:n], x) / get_f(el[n + 1:], x)) * znak
                            znak = 1
                    else:
                        summ += get_f(el, x) * znak
                        znak = 1
                else:
                    if el == '-':
                        znak = -1
        return summ


    def print_func(self, start=(y * -1), finish=y):
        if '^0.' in self.string and start < 0:
            start = 0
        clear()
        home()
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
        stamp()
        goto(0, 0)
        goto(0, y)
        lt(90)
        stamp()
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
        for i in range(start, finish - 1):
            if results[i - start]:
                goto(i, int(results[i - start] * step))
            else:
                pu()
                goto(i + 1, int(results[i - start + 1] * step))
                pd()


def handle_keypress(event):
    f = Function(entr.get())
    f.print_func()


button.bind("<Button-1>", handle_keypress)

fu = Function('x + 1')
print(fu.get_func(10))

mainloop()