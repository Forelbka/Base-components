import random


class cell():
    def __init__(self, x, y, value, matrix):
        self.x = x
        self.y = y
        self.value = value
        self.flaged = False
        self.hidden = True
        self.matr = matrix

    def __str__(self):
        return f'(x: {self.x}, y: {self.y}) = {self.value}'

    def set_value(self, value):
        self.value = value
    
    def get_value(self):
        if self.hidden:
            return '-'
        else:
            return self.value
    
    def get_neibours(self):
        matr = self.matr
        x = self.x
        y = self.y
        neibours = [[matr[x + i][y + j] for j in range(-1, 1) if x + i >= 0 and x + i < len(matr) and y + j >= 0 and y + j < len(matr[0])] for i in range(-1, 1)]
        return neibours
    
    def update(self):
        neibours = self.get_neibours()
        mine_count = 0
        for neib in neibours:
            if neib.get_value() == -1:
                mine_count += 1
        self.set_value(mine_count)
    
    def glob_update(self):
        self.update()
        map(lambda x: x.update(), self.get_neibours())
    
    def flag(self):
        if self.hidden:
            self.flag = not self.flag
    
    def glob_unhide(self):
        if self.value == -1:
            return 'Fale'
        self.hidden = False
        box = self.matr
        map(lambda x: x.glob_unhide(), [el for el in self.get_neibours() if box[el[0]][el[1]].value != 0])
        map(lambda x: x.unhide(), [el for el in self.get_neibours() if box[el[0]][el[1]].value != -1])
        self.glob_update()
    
    def unhide(self):
        box = self.matr
        map(lambda x: x.set_hidde(), [el for el in self.get_neibours() if box[el[0]][el[1]].value != -1])
    
    def set_hidde(self):
        self.hidden = False


print('Введите количество строк и столбцов поля или введите сложность легко, средне или сложно')
inp = input()
if inp == 'сложно':
    bx = 16
    by = 30
elif inp == 'среднe':
    bx = 16
    by = 16
elif inp == 'легко':
    bx = 9
    by = 9
else:
    bx, by = map(int, inp.split())

box = []
box = [[cell(i, j, 0, box) for j in range(by)] for i in range(bx)]

mines_count = int((bx * by) // 6.4)

for _ in range(mines_count):
    x = random.randint(0, bx - 1)
    y = random.randint(0, by - 1)
    box[x][y].set_value(-1)

hide_help = True

while True:
    if hide_help:
        print('Команда    значение')
        print('x y        открыть клетку')
        print('флаг x y   поставить или убрать флаг')
        print('скрыть     скрыть эту подсказку')
        print('показать     показать подсказку')
    
    inp = input()

    if inp == 'скрыть':
        hide_help = False
    elif inp == 'показать' or inp == 'help':
        hide_help = True

    inp = inp.split()

    if inp[0] == 'флаг':
        box[int(inp[1])][int(inp[2])].flag()
    elif len(inp) == 2:
        box[int(inp[0])][int(inp[1])].unhide()