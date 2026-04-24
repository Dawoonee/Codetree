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
    flag = True
elif a[0] < b[0]:
    flag = False
else:
    flag = 0
cnt = 0
for i in range(1, len(a)):
    if flag:
        if a[i] < b[i]:
            cnt += 1
            flag = False
        elif a[i] > b[i]:
            continue
        else:
            continue
    if not flag:
        if a[i] > b[i]:
            cnt += 1
            flag = True
        elif a[i] < b[i]:
            continue
        else:
            continue
print(cnt)