class matrix():
    def __init__(self, m) -> None:
        self.matr = m
    
    def __add__(self, other):
        m1 = self.matr
        m2 = other.matr
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            return 'Error 011'
        return matrix([[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))])
    
    def __sub__(self, other):
        m1 = self.matr
        m2 = other.matr
        if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
            return 'Error 012'
        return matrix([[m1[i][j] - m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))])
    
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return matrix([list(map(lambda x: x * other, self.matr[i])) for i in range(len(self.matr))])
        elif type(other) == matrix:
            m1 = self.matr
            m2 = other.matr
            m3 = [[0 for _ in range(len(m2[0]))] for i in range(len(m1))]
            if len(m1[0]) == len(m2):
                for i in range(len(m1)):
                    for j in range(len(m2[0])):
                        m3[i][j] = sum([m1[i][f] * m2[f][j] for f in range(len(m2))])
                return matrix(m3)
            else:
                return 'Error 021'
        else:
            return 'Error 022'
    
    def __truediv__(self, other):
        return 'Error 023'
    
    def __floordiv__(self, orher):
        return 'Error 024'
    
    def __mod__(self, other):
        return 'Error 025'
    
    def __divmod__(self, other):
        return 'Error 026'
    
    def __lt__(self, other):
        return len(self.matr) * len(self.matr[0]) < len(other.matr) * len(other.matr[0])
    
    def __eq__(self, other):
        if len(self.matr) == len(other.matr) and len(self.matr[0]) ==  len(other.matr[0]):
            flag = True
            for i in range(len(self.matr)):
                if self.matr[i] != other.matr[i]:
                    flag = False
            if flag:
                return True
        return False
    
    def __len__(self):
        return len(self.matr)
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, self.matr[i])) for i in range(len(self.matr))])
    
    def __repr__(self):
        return str(self.matr)
    
    def __getitem__(self, key):
        return self.matr[key]
    
    def __setitem__(self, key, el):
        self.matr[key] = el

tes1 = matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

tes2 = matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print(tes1[1])