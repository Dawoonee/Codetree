n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

arr = [[0]*201 for _ in range(201)]
point = 100

for i in range(n):
    for r in range(point + y[i] -8, point + y[i]):
        for c in range(point + x[i], point + x[i] + 8):
            arr[r][c] += 1

cnt = 0
for r in range(201):
    for c in range(201):
        if arr[r][c] >= 1:
            cnt += 1
print(cnt)