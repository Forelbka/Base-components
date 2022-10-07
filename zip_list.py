import random
import sys

class ziplist:
    def __init__(self, lis):
        self.lis = lis
        self.zipedlis = []
        self.repeats = []
        self.compress()
    def __add__(self, other):
        if other == ziplist:
            return ziplist(self.uncompress() + other.uncompress()).compress()
        elif other == list:
            return self.uncompress() + other
        else:
            return self.uncompress() + list(other)
    def __str__(self):
        return str(self.uncompress())
    def __repr__(self):
        return f'Compresse: {bool(self.zipedlis)}, Compressed List: {self.zipedlis}, Uncompressed List: {self.uncompress()}'
    def compress(self):
        combinations = []
        doubles = []
        for i in range(2, len(self.lis) // 2 + 1):
            for j in range(len(self.lis) - i + 1):
                combinations.append(self.lis[j : j + i])
        combinations = combinations[::-1]
        m = 0
        while m < len(combinations):
            combin = combinations[m]
            if combinations.count(combin) >= 2:
                doubles.append(combin)
                while combinations.count(combin) > 1:
                        combinations.pop(combinations.index(combin))
            m += 1
        
        for num, combin in enumerate(doubles):
            a = 0
            while a < len(self.lis) - 1:
                if self.lis[a] == combin[0]:
                    flag = True
                    for j in range(len(combin)):
                        if self.lis[a + j] != combin[j]:
                            flag = False
                    if flag:
                        self.lis = self.lis[:a] + [str(num)] + self.lis[a + len(combin):]
                    else:
                        flag = True
                        # doubles.pop(num)
                a += 1
        self.repeats = doubles
        self.zipedlis = self.lis
        self.lis = []

    def uncompress(self):
        for el in self.zipedlis:
            if type(el) == str:
                self.lis += self.repeats[int(el)]
            else:
                self.lis.append(el)
        return [self.lis.pop(0) for _ in range(len(self.lis))]


b = [random.randint(-10, 10) for _ in range(500)]
a = ziplist(b[:])
print(str(a) == str(b))
print(sys.getsizeof(a))
print(sys.getsizeof(b))