n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0]*(n+1) for _ in range(n+1)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
    cnt = 0
    y, x = points[i][0], points[i][1]
    grid[y][x] = 1
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < n+1 and 0 <= ny < n+1:
            if grid[ny][nx] == 1:
                cnt += 1
    if cnt >= 3:
        print(1)
    else:
        print(0)