from weakref import ref


def bablsort(lis):
    if len(lis) < 2:
        return(lis)
    for i in range(len(lis) - 1):
        flag = True
        for j in range(len(lis) - 1 - i):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                flag = False
        if flag:
            break
    return lis

def hairbrushsort(lis):
    if len(lis) < 2:
        return(lis)
    dounfactor = 1.2470
    dist = len(lis) / dounfactor
    distance_ = int(abs(dist))

    while True:
        flag = True
        for i in range(len(lis) - distance_):
            if lis[i] > lis[i + distance_]:
                lis[i], lis[i + distance_] = lis[i + distance_], lis[i]
                flag = False
            print(lis)
        if flag and distance_ == 1:
            return lis
        dist /= dounfactor
        distance_ = int(abs(dist))

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

def fastsort(lis):
    if len(lis) < 2:
        return(lis)
    ref_el = lis.pop(len(lis) // 2)
    new_lis = [lis[i] for i in range(len(lis)) if lis[i] < ref_el]
    lis = [el for el in lis if not el in new_lis]
    return fastsort(new_lis) + [ref_el] + fastsort(lis)


print(fastsort([1, 2, -10, 7, 0, 100, 10, -100]))