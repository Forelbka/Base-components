f = open('p27_3_b.txt')
l = f.readlines()

def de(n):
    if int(n) % 2 == 0:
        return 1
    return -1

l = list(map(de, l))

heights = {0: -1}
h = 0
maxlen = 0

for i in range(len(l)):
    if h + l[i] in heights:
        h += l[i]
        maxlen = max(maxlen, i - heights[h])
    else:
        h += l[i]
        heights[h] = i

print(maxlen)