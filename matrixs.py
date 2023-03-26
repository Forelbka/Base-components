class matrix():
    def __init__(self, m) -> None:
        self.matr = m
    
    def transpon(self):
        return [[self.matr[j][i] for j in range(len(self.matr))] for i in range(len(self.matr[0]))]
    
    def determinant(self):
        matr = self.matr
        if len(matr) != len(matr[0]):
            return 'Error'
        if len(matr) == 1:
            return matr[0][0]
        if len(matr) == 2:
            return matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0]
        det = 0
        for i in range(len(matr)):
            det += ((-1) ** i) * matrix([el[:-1] for n, el in enumerate(matr) if n != i]).determinant() * matr[i][-1]
        return det * ((-1) ** (len(matr) - 1))
    
    def kramer(self, free):
        matr = self.matr
        det = self.determinant()
        if det == 0:
            return 'No consistent solution'
        ret = []
        for i in range(len(matr)):
            new_matrix = self.transpon()
            new_matrix[i] = free
            new_matrix = matrix(new_matrix).transpon()
            ret.append(matrix(new_matrix).determinant() // det)
        return ' '.join(map(str, ret))
 
    def revers_matrix(self):
        matr = self.matr
        minor_matr = []
        if len(matr) != len(matr[0]):
            return 'Error'
        for i in range(len(matr)):
            minor_matr.append([])
            for j in range(len(matr[-1])):
                minor_matr[-1].append(matrix([el[:j] + el[j + 1:] for n, el in enumerate(matr) if n != i]).determinant() * ((-1) ** i)* ((-1) ** j) * (-1))
        return matrix(minor_matr).transpon()
    
    def set_zero(self):
        self.matr = [[0 for i in range(len(self.matr[0]))] for _ in range(len(self.matr))]
    
    def set_singl(self):
        if len(self.matr) != len(self.matr[0]):
            return 'Error'
        self.matr = [[0 for i in range(len(self.matr[0]))] for _ in range(len(self.matr))]
        for i in range(min((len(self.matr), len(self.matr[0])))):
            self.matr[i][i] = 1
 
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
    [3, -3, -5, 8],
    [-3, -5, -7, 5],
    [2, -5, -7, 7],
    [-4, 3, 5, -6]
])
 
tes2 = matrix([list(map(int, input().split())) for _ in range(int(input()))])


 
print(tes1.set_singl())
print(tes1)