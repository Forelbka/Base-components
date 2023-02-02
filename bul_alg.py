from itertools import product

signs = {
    '→': ' → ',
    '∧': ' * ',
    '∨': ' + ',
    '¯¯¯': 'not ',
    '(': '(',
    ')': ')'
}

def f(func, values):

    variables = sorted(list(set([el for el in func if el not in signs.keys() and el != '¯'])))

    for i, val in enumerate(values):
        func = func.replace(variables[i], str(val))
    
    for l1, l2 in signs.items():
        func = func.replace(l1, l2)
    return func

def getf(func):
    func = str(func)
    # func = ' ' + ' '.join(func.split()) + ' '
    while set(func.split()) & set(map(lambda x: str(x.split()[0]) , signs.values())):
        if '(' in func:
            br_f = func.find('(')
            br_l = len(func) - func[::-1].find(')')
            func = func[:br_f] + getf(func[br_f + 1: br_l - 1]) + func[br_l:]
        elif 'not' in func:
            ind = func.find('not')
            func = func[:ind] + str(int(not(int(func[ind + 4])))) + func[ind + 5:]
        elif '<=' in func:
            ind = func.find('→')
            f1 = int(getf(func[:ind - 1]))
            f2 = int(getf(func[ind + 2:]))
            func = not f1 or f2
        elif '+' in func:
            ind = func.find('+')
            f1 = int(getf(func[:ind - 1]))
            f2 = int(getf(func[ind + 2:]))
            func = str(f1 or f2)
        elif '*' in func:
            ind = func.find('*')
            f1 = int(getf(func[:ind - 1]))
            f2 = int(getf(func[ind + 2:]))
            func = str(f1 and f2)
    return func
 
st = 'A∧(C∨¯¯¯B)∧¯¯¯C'


print(*sorted(list(set([el for el in st if el not in signs.keys() and el != '¯']))), 'F', sep='  ')
print()

for v in product((0, 1), repeat=len(list(set([el for el in st if el not in signs.keys() and el != '¯'])))):
    fu = f(st, v)
    print(*v, getf(fu), sep='  ')
