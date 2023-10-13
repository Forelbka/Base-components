def poland_to_normal(string):
    ret = []
    for sim in string:
        try:
            ret.append(float(sim))
        except:
            if sim == '+':
                ret.append(ret.pop(-1) + ret.pop(-1))
            elif sim == '-':
                ret.append(ret.pop(-2) - ret.pop(-1))
            elif sim == '*':
                ret.append(ret.pop(-1) * ret.pop(-1))
            elif sim == '/':
                ret.append(ret.pop(-1) - ret.pop(-1))
    return ret[-1]

def check_stack(stack_):
    if not stack_:
        return 0
    if stack_[-1] == '(':
        return 1
    if stack_[-1] == '+' or stack_[-1] == '-':
        return 2
    if stack_[-1] == '*' or stack_[-1] == '/':
        return 3

def normal_to_poland(string):
    ret = []
    stack_ = []
    for sim in string:
        try:
            ret.append(float(sim))
        except:
            if sim in ('*', '/', '+', '-'):
                if check_stack(stack_) == 0 or check_stack([sim]) > check_stack(stack_):
                    stack_.append(sim)
                elif check_stack([sim]) <= check_stack(stack_):
                    while check_stack([sim]) <= check_stack(stack_):
                        ret.append(stack_.pop(-1))
                    stack_.append(sim)
            if sim == '(':
                stack_.append(sim)
            if sim == ')':
                while stack_[-1] != '(':
                    ret.append(stack_.pop(-1))
                stack_.pop(-1)
    ret += stack_
    return ' '.join(map(str, ret))

def cringe_to_base(cringe:str):
    replase_dict = {
        '-': ' - ',
        '+': ' + ',
        '*': ' * ',
        '/': ' / ',
        '(': ' ( ',
        ')': ' ) '
    }
    for key, var in replase_dict.items():
        cringe = cringe.replace(key, var)
    return cringe.split()


print(normal_to_poland(cringe_to_base('(1+2)*3')))
print(normal_to_poland(cringe_to_base('1+2*3')))
print(normal_to_poland(cringe_to_base('(1+2*4)-3*5+6')))
print(normal_to_poland(cringe_to_base('1+2*(4-3*5)+6')))
