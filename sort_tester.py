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
def choiseSort(lis):
    for i in range(len(lis)):
        minim = i
        for j in range(i, len(lis)):
            if lis[j] < lis[minim]:
                minim = j
        lis[i], lis[minim] = lis[minim], lis[i]
    return lis
# Функция сортировки

# test_sort(функция без скобок, repeats=кол-во повторов больших тестов, lens=[список из возможных длинн тестовых списков])

test_sort(choiseSort, repeats=10, lens=[1000])