import random
import datetime

def test_sorf(func, repeats=10, lens=[1000]):
    print('Простейшие тесты:')
    print(f'При {[]}  ----  {func([])}')
    print(f'При {[1]}  ----  {func([1])}')
    print(f'При {[2, 1]}  ----  {func([2, 1])}')
    flag = True
    for _ in range(repeats):
        sorted_list = [-10, 0, 10]
        for i in range(random.choice(lens) - 3):
            sorted_list.append(random.randint(-10000, 10000))
        now = datetime.datetime.now()
        after_sort = func(sorted_list)
        after = datetime.datetime.now()
        if after_sort == sorted(sorted_list):
            print(f'Список на {len(sorted_list)} элеменотов отсортирован за {after - now}  ВЕРНО!')
        else:
            print(f'Список на {len(sorted_list)} элеменотов отсортирован за {after - now}  НЕВЕРНО!\nисходный список: {sorted_list}\nВыходной Список: {after_sort}')
            flag = False
    if flag:
        print('Крупные тесты верны')
    else:
        print('Крупные тесты не верны')

# Функция сортировки
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

test_sorf(insertsort)