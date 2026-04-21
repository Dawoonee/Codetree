
m1, d1, m2, d2 = map(int, input().split())
a = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d = m1, d1
cnt = 1
while True:
    if m == m2 and d == d2:
        break
    if a[m] == d:
        m += 1
        d = 1
    else:
        d += 1
    cnt += 1
print(cnt)