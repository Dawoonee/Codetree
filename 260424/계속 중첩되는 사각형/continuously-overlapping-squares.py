n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
arr = [[0]*201 for _ in range(201)]
point = 100
flag = True
for i in range(n):
    if flag:
        for y in range(point + y1[i], point + y2[i]):
            for x in range(point + x1[i], point + x2[i]):
                arr[y][x] = 'R'
        flag = False
    else:
        for y in range(point + y1[i], point + y2[i]):
            for x in range(point + x1[i], point + x2[i]):
                arr[y][x] = 'B'
        flag = True

cnt = 0
for r in range(201):
    for c in range(201):
        if arr[r][c] == 'B':
            cnt += 1
print(cnt)