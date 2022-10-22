from hashlib import new
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

def choiseSort(lis):
    for i in range(len(lis)):
        minim = i
        for j in range(i, len(lis)):
            if lis[j] < lis[minim]:
                minim = j
        lis[i], lis[minim] = lis[minim], lis[i]
    return lis

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

