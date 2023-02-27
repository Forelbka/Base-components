import random
import sys

# Create a a list compression function
def compress(lst):
    # Create a new list
    compressed_list = []
    # Loop through the list
    for i in range(len(lst)):
        # If the next item is the same as the current item
        if i != len(lst) - 1 and lst[i] == lst[i + 1]:
            # Add the current item to the compressed list
            compressed_list.append(lst[i])
        else:
            # Add the current item to the compressed list
            compressed_list.append(lst[i])
            # Add a new item to the compressed list
            compressed_list.append(1)
    # Return the compressed list
    return compressed_list



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
        l = []
        for combin in doubles:
            a = 0
            n = 0
            while a < len(self.lis) - 1:
                if self.lis[a] == combin[0]:
                    if self.lis[a : a + len(combin)] == combin:
                        if combin in l:
                            self.lis = self.lis[:a] + [str(l.index(combin))] + self.lis[a + len(combin):]
                        else:
                            self.lis = self.lis[:a] + [str(n)] + self.lis[a + len(combin):]
                            l.append(combin)
                            n += 1
                a += 1
        doubles = l
        #print(doubles)
        #print(l)
        #li = [int(el) for el in self.zipedlis if type(el) == str]
        #doubles = [doubles[i] for i in range(len(doubles)) if i in li]
        # print(bs)
        #print(doubles)
        # print(self.lis)
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


b = [random.randint(0, 20) for _ in range(50)]
a = ziplist(b[:])
print(a.uncompress() == b)
print(a)
print(b)
print(a.zipedlis)
print(a.repeats)
print([int(el) for el in a.zipedlis if type(el) == str])
print(sys.getsizeof(a.zipedlis) + sys.getsizeof(a.repeats))
print(sys.getsizeof(b))