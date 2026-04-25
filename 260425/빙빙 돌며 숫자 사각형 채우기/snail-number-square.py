n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0
x, y = 0, 0
num = 2
arr[0][0] = 1
while num <= n*m:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 0:
        arr[ny][nx] = num
        num += 1
        x, y = nx, ny
    else:
        d += 1
        if d == 4:
            d = 0
for i in range(n):
    print(' '.join(map(str, arr[i])))