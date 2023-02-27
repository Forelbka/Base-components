import tkinter as tk


class cell():
    def __init__(self, coordinates):
        self.status = ' '
        self.win = False
        self.coordinates = coordinates
    
    def set_status(self, status):
        self.status = status
    
    def set_win(self, win):
        self.win = win
    
    def get_status(self):
        return self.status
    
    def get_win(self):
        return self.win
    
    # def get_neighbors(self):
    #     neighbors = [
    #         [[self.coordinates[0] - 1, self.coordinates[1]], [self.coordinates[0] + 1, self.coordinates[1]]],
    #         [[self.coordinates[0], self.coordinates[1] - 1], [self.coordinates[0], self.coordinates[1] + 1]],
    #         [[self.coordinates[0] - 1, self.coordinates[1] - 1], [self.coordinates[0] + 1, self.coordinates[1] + 1]],
    #         [[self.coordinates[0] - 1, self.coordinates[1] + 1], [self.coordinates[0] + 1, self.coordinates[1] - 1]]
    #     ]
    #     return [nei for nei in neighbors if nei[0][0] >= 0 and nei[0][0] < 3 and nei[0][1] >= 0 and nei[0][1] < 3 and nei[1][0] >= 0 and nei[1][0] < 3 and nei[1][1] >= 0 and nei[1][1] < 3]
    
    

box = [
    [cell([0, 0]), cell([0, 1]), cell([0, 2])],
    [cell([1, 0]), cell([1, 1]), cell([1, 2])],
    [cell([2, 0]), cell([2, 1]), cell([2, 2])],
    ]

def win(status):
    global box, st
    print(f'win {st}!')
    box = [
    [cell([0, 0]), cell([0, 1]), cell([0, 2])],
    [cell([1, 0]), cell([1, 1]), cell([1, 2])],
    [cell([2, 0]), cell([2, 1]), cell([2, 2])],
    ]


def set_cell(y ,x , status):
    if box[y][x].get_win() == status:
        win(status)
    else:
        box[y][x].set_status(status)
        combins = [
            [box[0][0], box[0][1], box[0][2]],
            [box[1][0], box[1][1], box[1][2]],
            [box[2][0], box[2][1], box[2][2]],
            [box[0][0], box[1][0], box[2][0]],
            [box[0][1], box[1][1], box[2][1]],
            [box[0][2], box[1][2], box[2][2]],
            [box[0][0], box[1][1], box[2][2]],
            [box[0][2], box[1][1], box[2][0]],
        ]
        for n, com in enumerate([list(map(lambda x: x.get_status(), combin)) for combin in combins]):
            if com.count(status) == 2:
                for d, c in enumerate(com):
                    if c != status:
                        combins[n][d].set_win(status)

    for el in [list(map(lambda x: x.get_status(), combin)) for combin in box]:
        print(*el)
    
    global labels, st
    labels[y][x]['text'] = status
    if st == '0':
        st = '✖'
    else:
        st = '0'
    

 
window = tk.Tk()
window.title("Крестики - нолики")
window.geometry('900x900')

st = '0'

labels = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=3
        )
        frame.grid(row=i, column=j)
        labels[i][j] = tk.Button(master=frame, text=box[i][j].get_status(), command=lambda x=i, y=j: set_cell(x, y, st), width=8, height=4, font='Times 30')
        labels[i][j].pack()


window.mainloop()