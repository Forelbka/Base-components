import tkinter as tk

# создание окна приложения
root = tk.Tk()
root.title('Калькулятор')

# создание поля для ввода
entry = tk.Entry(root, width=25, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# создание функций для кнопок
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)

if math == 'addition':
    entry.insert(0, f_num + float(second_number))
elif math == 'subtraction':
    entry.insert(0, f_num - float(second_number))
elif math == 'multiplication':
    entry.insert(0, f_num * float(second_number))
elif math == 'division':
    entry.insert(0, f_num / float(second_number))

# создание кнопок
button_1 = tk.Button(root, text='1', padx=20, pady=10, command=lambda: button_click(1))
button_1.grid(row=1, column=0)

button_2 = tk.Button(root, text='2', padx=20, pady=10, command=lambda: button_click(2))
button_2.grid(row=1, column=1)

button_3 = tk.Button(root, text='3', padx=20, pady=10, command=lambda: button_click(3))
button_3.grid(row=1, column=2)

button_4 = tk.Button(root, text='4', padx=20, pady=10, command=lambda: button_click(4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(root, text='5', padx=20, pady=10, command=lambda: button_click(5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(root, text='6', padx=20, pady=10, command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_7 = tk.Button(root, text='7', padx=20, pady=10, command=lambda: button_click(7))
button_7.grid(row=3, column=0)

button_8 = tk.Button(root, text='8', padx=20, pady=10, command=lambda: button_click(8))
button_8.grid(row=3, column=1)

button_9 = tk.Button(root, text='9', padx=20, pady=10, command=lambda: button_click(9))
button_9.grid(row=3, column=2)

button_0 = tk.Button(root, text='0', padx=20, pady=10, command=lambda: button_click(0))
button_0.grid(row=4, column=0)

button_clear = tk.Button(root, text='C', padx=20, pady=10, command=button_clear)
button_clear.grid(row=4, column=1)

button_equal = tk.Button(root, text='=', padx=20, pady=10, command=button_equal)
button_equal.grid(row=4, column=2)

button_plus = tk.Button(root, text='+', padx=20, pady=10, command=button_add)
button_plus.grid(row=1, column=3)

button_minus = tk.Button(root, text='-', padx=20, pady=10, command=button_subtract)
button_minus.grid(row=2, column=3)

button_multiply = tk.Button(root, text='*', padx=20, pady=10, command=button_multiply)
button_multiply.grid(row=3, column=3)

button_divide = tk.Button(root, text='/', padx=20, pady=10, command=button_divide)
button_divide.grid(row=4, column=3)

root.mainloop()