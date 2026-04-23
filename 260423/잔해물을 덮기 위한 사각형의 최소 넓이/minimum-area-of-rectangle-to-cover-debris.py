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

cnt = 0
for y in range(2001):
    for x in range(2001):
        if arr[y][x] >= 1:
            cnt += 1
print(cnt)