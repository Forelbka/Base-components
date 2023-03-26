import tkinter as tk
from math import pi, log2

buttons = {
    (0, 0): 'log',
    (0, 1): '(',
    (0, 2): '7',
    (0, 3): '4',
    (0, 4): '1',
    (0, 5): '0',
    (1, 0): '𝝅',
    (1, 1): ')',
    (1, 2): '8',
    (1, 3): '5',
    (1, 4): '2',
    (1, 5): '000',
    (2, 0): '<',
    (2, 1): '^',
    (2, 2): '9',
    (2, 3): '6',
    (2, 4): '3',
    (2, 5): '.',
    (3, 0): 'C',
    (3, 1): '/',
    (3, 2): '*',
    (3, 3): '-',
    (3, 4): '+',
    (3, 5): '=',
}

def evaluate_expression(exp):
    if exp == '':
        return 0
    
    if '𝝅' in exp:
        i = exp.index('𝝅')
        exp = exp[:i] + str(pi) + exp[i + 1:]
    
    
    signs = ['+', '-', '/', '^', '*']
    sep_exp = [exp[0]]
    l_bracket = 0
    r_bracket = 0

    if exp[0] == '(':
        l_bracket += 1
    elif exp[0] == ')':
        r_bracket += 1
    
    for i in range(1, len(exp)):
        if exp[i] == '(':
            l_bracket += 1
        
        elif exp[i] == ')':
            r_bracket += 1
        
        if l_bracket != r_bracket:
            sep_exp[-1] += exp[i]
        
        elif exp[i] in signs:
            sep_exp.append(exp[i])
        
        else:
            if sep_exp[-1] in signs:
                sep_exp.append(exp[i])
            else:
                sep_exp[-1] += exp[i]
        
    for i, el in enumerate(sep_exp):
        if '(' in el:
            sep_exp[i] = evaluate_expression(el[1: -1])
    
    while '^' in ''.join(sep_exp):
        i = sep_exp.index('^')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) ** float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '*' in ''.join(sep_exp):
        i = sep_exp.index('*')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) * float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '/' in ''.join(sep_exp):
        i = sep_exp.index('/')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) / float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '+' in ''.join(sep_exp):
        i = sep_exp.index('+')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) + float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '-' in ''.join(sep_exp):
        i = sep_exp.index('-')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) - float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
            
    return sep_exp[0]



window = tk.Tk()
window.title('Calculator')
window.geometry('411x520')
window.resizable(False, False)

# entry = tk.Entry(width=400)
# entry.pack(side=tk.TOP)

for i in range(2, 8):
    for j in range(4):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Button(master=frame, text=buttons[(j, i - 2)], fg='black', bg='white', width=13, height=4, command=lambda p = i - 2, q = j: entr.insert(tk.END, buttons[(q, p)]))
        label.pack()

entr = tk.Entry(width=67)
entr.grid(row=0, column=0, columnspan=4)

res = tk.Label(width=50, height=4, text='Res')
res.grid(row=1, column=0, columnspan=4)

tk.Button(width=13, height=4,text='>', command=lambda: entr.delete(len(entr.get()) - 1, tk.END)).grid(row=2, column=2)
tk.Button(width=13, height=4,text='C', command=lambda: entr.delete(0, tk.END)).grid(row=2, column=3)
tk.Button(width=13, height=4,text='=', command=lambda: res.config(text=evaluate_expression(entr.get()))).grid(row=7, column=3)
tk.Button(width=13, height=4,text='log', command=lambda: entr.insert(tk.END, 'l(')).grid(row=2, column=0)

window.mainloop()