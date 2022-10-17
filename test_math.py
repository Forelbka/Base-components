def get_f(strin, x):
    strin = strin[:]
    l_rez = 1
    if 'x' in strin:
        if not '^' in strin:
            l_rez *= x
        strin = strin.split('x')
        if strin[0]:
            if strin[0] == '-':
                l_rez *= -1
            else:
                l_rez *= float(strin[0])
        if strin[1]:
            l_rez *= x ** float(strin[1][1:])
    else:
        l_rez *= float(strin)
    return l_rez

def gett_f(strin, x):
    znak = 1
    summ = 0
    l_sum = 1
    if '(' in strin or ')' in strin:
                count_s = 0
                ind_f = strin.find('(')
                if strin[0] != '(':
                    l_sum *= get_f(strin[:ind_f], x)
                for n, zn in enumerate(strin[ind_f:]):
                    if zn == '(':
                        count_s += 1
                    elif zn == ')':
                        count_s -= 1
                    if count_s == 0:
                        if n != len(strin[ind_f:]) - 1:
                            summ += (gett_f(strin[ind_f + 1:n], x) + gett_f(strin[n + 1:], x)) * l_sumh
                        else:
                            summ += gett_f(strin[ind_f + 1:n], x)
                        break
    else:
        strin = strin.split()
        for el in strin:
            if len(el) > 1 or el == 'x' or el in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if '/' in el:
                    n = el.find('/')
                    if get_f(el[n + 1:], x) == 0:
                        return None
                    else:
                        summ += (get_f(el[:n], x) / get_f(el[n + 1:], x)) * znak
                        znak = 1
                else:
                    summ += get_f(el, x) * znak
                    znak = 1
            else:
                if el == '-':
                    znak = -1
    return summ


print(gett_f('2(x + 1)', 10))