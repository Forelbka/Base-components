import random
import datetime

from sorts import insertsort

def test_sort(func, repeats=10, lens=[1000]):
    print('Простейшие тесты:')
    print(f'При {[]}  ----  {func([])}')
    print(f'При {[1]}  ----  {func([1])}')
    print(f'При {[2, 1]}  ----  {func([2, 1])}')
    print('\n\n\n')
    flag = True
    for _ in range(repeats):
        sorted_list = [-10, 0, 10]
        for i in range(random.choice(lens) - 3):
            sorted_list.append(random.randint(-10000, 10000))
        random.shuffle(sorted_list)
        sor = sorted_list[:]
        now = datetime.datetime.now()
        after_sort = func(sor)
        after = datetime.datetime.now()
        if after_sort == sorted(sorted_list):
            print(f'Список на {len(sorted_list)} элеменотов отсортирован за {after - now}  ВЕРНО!')
        else:
            print(f'Список на {len(sorted_list)} элеменотов отсортирован за {after - now}  НЕВЕРНО!\nИсходный список: {sorted_list}\nВыходной Список: {after_sort}\nСортированный:   {sorted(sorted_list)}')
            flag = False
        print('\n')
    if flag:
        print('Крупные тесты верны')
    else:
        print('Крупные тесты не верны')

# Функция сортировки
class heap():
    def __init__(self, lis=[]):
        self.lis = []
        if lis:
            for el in lis:
                self.insert(el)
    def siftUp(self, i=None):
        if i is None:
            i = len(self.lis) - 1
        p = (i - 1) // 2
        lis = self.lis
        while i > 0 and lis[p] > lis[i]:
            lis[p], lis[i] = lis[i], lis[p]
            i = p
            p = (i - 1) // 2
        self.lis = lis
    def siftDoun(self, i=0):
        l = i * 2 + 1
        r = i * 2 + 2
        lis = self.lis
        p = i
        while True:
            if l < len(lis) and lis[p] > lis[l]:
                p = l
            if r < len(lis) and lis[p] > lis[r]:
                p = r
            if i == p:
                break
            lis[i], lis[p] = lis[p], lis[i]
            i = p
            l = i * 2 + 1
            r = i * 2 + 2
        self.lis = lis
    def insert(self, el):
        self.lis.append(el)
        self.siftUp()
    def getMin(self):
        lis = self.lis
        minn = lis[0]
        lis[0], lis[-1] = lis[-1], lis[0]
        lis.pop()
        self.lis = lis
        self.siftDoun()
        return minn

def heapSort(lis):
    heap_ = heap(lis)
    return [heap_.getMin() for _ in range(len(lis))]
# Функция сортировки

# test_sort(функция без скобок, repeats=кол-во повторов больших тестов, lens=[список из возможных длинн тестовых списков])

test_sort(heapSort, repeats=5, lens=[10])