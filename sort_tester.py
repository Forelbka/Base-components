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
    return lis
# Функция сортировки

# test_sort(функция без скобок, repeats=кол-во повторов больших тестов, lens=[список из возможных длинн тестовых списков])

test_sort(mergeSort, repeats=10, lens=[1000])