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

    variables = sorted(list(set([el for el in func if el not in signs.values()])))

    for i, val in enumerate(values):
        func = func.replace(variables[i], str(val))
    
    for l1, l2 in signs.items():
        func = func.replace(l1, l2)
    return func

def getf(func, values):
    func = str(func)
    while set(func) | set(signs.values()):
        if '(' in func:
            br_f = func.find('(')
            br_l = len(func) - func[::-1].find(')')
            func = func[:br_f] + getf(func[br_f: br_l], values) + func[br_l:]
        elif 'not' in func:
            ind = func.find('not')
            func = func[:ind] + str(int(not(func[ind + 4]))) + func[:ind + 5]
        elif '*' in func:
            ind = func.find('*')
            func = func[:ind - 2] + str(int(func[ind - 2] and func[ind + 2])) + func[ind + 3:]
        elif '+' in func:
            ind = func.find('+')
            func = func[:ind - 2] + str(int(func[ind - 2] or func[ind + 2])) + func[ind + 3:]
        elif '<=' in func:
            ind = func.find('→')
            func = func[:ind - 2] + str(int(not(func[ind - 2]) or func[ind + 2])) + func[ind + 3:]
        func = ' ' + ' '.join(func.split()) + ' '
    return func

fu = f('A∧C∨¯¯¯A∧¯¯¯C', (0, 1, 0))
print(fu)
print(getf(fu, (0, 1, 0)))