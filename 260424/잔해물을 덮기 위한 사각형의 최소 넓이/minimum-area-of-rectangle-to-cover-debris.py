x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

arr = [[0]*2001 for _ in range(2001)]
point = 1000

for y in range(point + y1[0], point + y2[0]+1):
    for x in range(point + x1[0], point + x2[0]+1):
        arr[y][x] += 1
for y in range(point + y1[1], point + y2[1]+1):
    for x in range(point + x1[1], point + x2[1]+1):
        arr[y][x] -= 1

cnt = []
for y in range(2001):
    for x in range(2001):
        if arr[y][x] == 1:
            cnt.append((x, y))
a, b, c, d = 0, 2001, 0, 2001
# print(cnt)
if len(cnt) == 0:
    print(0)
else:
    for x, y in cnt:
        a = max(a, x)
        b = min(b, x)
        c = max(c, y)
        d = min(d, y)
    # print(a, b, c, d)
    answer = (a-b)*(c-d)
    print(answer)