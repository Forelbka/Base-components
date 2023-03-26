def evaluate_expression(exp):
    signs = ['+', '-', '/', '^', '*']
    sep_exp = [exp[0]]
    l_bracket = 0
    r_bracket = 0
    if exp[0] == '(':
        l_bracket += 1
    elif exp[0] == ')':
        r_bracket += 1
    
    for i in range(1, len(exp)):
        if exp[i] == '(':
            l_bracket += 1
        
        elif exp[i] == ')':
            r_bracket += 1
        
        if l_bracket != r_bracket:
            sep_exp[-1] += exp[i]
        
        elif exp[i] in signs:
            sep_exp.append(exp[i])
        
        else:
            if sep_exp[-1] in signs:
                sep_exp.append(exp[i])
            else:
                sep_exp[-1] += exp[i]
        
    for i, el in enumerate(sep_exp):
        if '(' in el:
            sep_exp[i] = evaluate_expression(el[1: -1])
    
    while '^' in ''.join(sep_exp):
        i = sep_exp.index('^')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) ** float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '*' in ''.join(sep_exp):
        i = sep_exp.index('*')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) * float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '/' in ''.join(sep_exp):
        i = sep_exp.index('/')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) / float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '+' in ''.join(sep_exp):
        i = sep_exp.index('+')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) + float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
    
    while '-' in ''.join(sep_exp):
        i = sep_exp.index('-')
        sep_exp[i - 1] = str(float(sep_exp[i - 1]) - float(sep_exp[i + 1]))
        del sep_exp[i + 1]
        del sep_exp[i]
            
    return sep_exp[0]

# print(evaluate_expression('2^3+4.5*5'))