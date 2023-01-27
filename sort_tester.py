import random
import datetime
import time

def test_sort(funcs, repeats=10, lens=[1000], mode='accuracy'):
    if mode == 'accuracy':
        for func in funcs:
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
    elif mode == 'speed':
        times = []
        tipe_of_tests = ['sorted', 'revers', 'big', 'smol']
        for nn, func in enumerate(funcs):
            times.append([str(func).split()[1]])
            for n, tipe_ in enumerate(tipe_of_tests):
                times[nn].append([tipe_])
                if tipe_ == 'sorted':
                    for _ in range(repeats):
                        lis = sorted([random.randint(-10000, 10000) for __ in range(10000)])
                        now = time.time()
                        func(lis)
                        times[nn][n + 1].append(time.time() - now)
                elif tipe_ == 'revers':
                    for _ in range(repeats):
                        lis = sorted([random.randint(-10000, 10000) for __ in range(500000)], reverse=True)
                        now = time.time()
                        func(lis)
                        times[nn][n + 1].append(time.time() - now)
                elif tipe_ == 'big':
                    for _ in range(repeats):
                        lis = [random.randint(-10000, 10000) for __ in range(10000)]
                        now = time.time()
                        func(lis)
                        times[nn][n + 1].append(time.time() - now)
                elif tipe_ == 'smol':
                    for _ in range(repeats):
                        lis = [random.randint(-10000, 10000) for __ in range(100)]
                        now = time.time()
                        func(lis)
                        times[nn][n + 1].append(time.time() - now)
        for funcs in times:
            print('=====================')
            for test in funcs[1:]:
                print(f'Функция: {funcs[0]} Тест: {test[0]} Результат: {sum(test[1:]) / len(test[1:])}')

# Функция сортировки
def fastsort(lis):
    if len(lis) < 2:
        return(lis)
    ref_el = lis.pop(len(lis) // 2)
    new_lis = [lis[i] for i in range(len(lis)) if lis[i] < ref_el]
    lis = [el for el in lis if not el in new_lis]
    return fastsort(new_lis) + [ref_el] + fastsort(lis)

def merge(lis1, lis2):
    i1, i2 = 0, 0
    new_lis = []
    while i1 != len(lis1) and i2 != len(lis2):
        if lis1[i1] < lis2[i2]:
            new_lis.append(lis1[i1])
            i1 += 1
        else:
            new_lis.append(lis2[i2])
            i2 += 1
    if i1 == len(lis1):
        return new_lis + lis2[i2:]
    return new_lis + lis1[i1:]

def mergeSort(lis):
    if len(lis) <= 1:
        return lis
    return merge(mergeSort(lis[:len(lis) // 2]), mergeSort(lis[len(lis) // 2:]))

def choiseSort(lis):
    for i in range(len(lis)):
        minim = i
        for j in range(i, len(lis)):
            if lis[j] < lis[minim]:
                minim = j
        lis[i], lis[minim] = lis[minim], lis[i]
    return lis

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

def insertsort(lis):
    if len(lis) < 2:
        return(lis)
    new_list = [lis[0]]
    for el in lis[1:]:
        for i in range(len(new_list)):
            if el <= new_list[i]:
                new_list.insert(i, el)
                break
            elif i == len(new_list) - 1:
                new_list.append(el)
    return new_list
# Функция сортировки

# test_sort(функция без скобок, repeats=кол-во повторов больших тестов, lens=[список из возможных длинн тестовых списков])

print(1)
test_sort([fastsort, choiseSort], repeats=10, lens=[10], mode='speed')