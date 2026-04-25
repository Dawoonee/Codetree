n, m = map(int, input().split())

v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

#x, y를 기록해서 걍 Y 높은쪽 어떰?
a = []
pos_a = 0
for x in range(n):
    for _ in range(t[x]):
        pos_a += v[x]
        a.append(pos_a)
b = []
pos_b = 0
for x in range(m):
    for _ in range(t2[x]):
        pos_b += v2[x]
        b.append(pos_b)
if a[0] > b[0]:
    flag = 'A'
elif a[0] < b[0]:
    flag = 'B'
else:
    flag = 'C'
cnt = 1
for i in range(1, len(a)):
    if flag == 'C':
        if a[i] > b[i]:
            flag = 'A'
            cnt += 1
        elif a[i] < b[i]:
            flag = 'B'
            cnt += 1
        else:
            continue
    elif flag == 'A' :
        if a[i] > b[i]:
            continue
        elif a[i] < b[i]:
            cnt += 1
            flag = 'B'
        else:
            cnt += 1
            flag = 'C'
    elif flag == 'B':
        if a[i] > b[i]:
            cnt += 1
            flag = 'A'
        elif a[i] < b[i]:
            continue
        else:
            cnt += 1
            flag = 'C'
print(cnt)