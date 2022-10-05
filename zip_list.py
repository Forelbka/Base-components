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
        for el in set(self.lis):
            if self.lis.count(el) > 1:
                self.repeats.append(el)
        for el in self.lis:
            if el in self.repeats:
                self.zipedlis.append(str(self.repeats.index(el)))
            else:
                self.zipedlis.append(el)
        self.lis = []
    def uncompress(self):
        for el in self.zipedlis:
            if type(el) == str:
                self.lis.append(self.repeats[int(el)])
            else:
                self.lis.append(el)
        return [self.lis.pop(0) for _ in range(len(self.lis))]
    
a = ziplist([1, 2, 5, 4, 7, 1, 1, 2, 2, 7, 7, 7])
print(a)
print(repr(a))
print(a.uncompress())