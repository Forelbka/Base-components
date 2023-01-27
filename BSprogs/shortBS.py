a = int(input())
b = int(input())
c = int(input())
k = int(input())
fp = []
sp = []
tp = []
i = 1
for j in range(max((a, b, c)) * 3):
    if j // 3 < a:
        fp.append(i)
        i += 1
    else:
        fp.append(0)
for j in range(max((a, b, c)) * 3):
    if j // 3 < b:
        sp.append(i)
        i += 1
    else:
        sp.append(0)
for j in range(max((a, b, c)) * 3):
    if j // 3 < c:
        tp.append(i)
        i += 1
    else:
        tp.append(0)
et = fp[3 * (k - 1): 3 * (k - 1) + 3] + sp[3 * (k - 1): 3 * (k - 1) + 3] + tp[3 * (k - 1): 3 * (k - 1) + 3]
et = [el for el in et if el != 0]
print(*et, sep='\n')