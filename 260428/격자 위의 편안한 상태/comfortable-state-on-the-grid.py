n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0]*(n+1) for _ in range(n+1)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
    cnt = 0
    r, c = points[i][0], points[i][1]
    grid[r][c] = 1
    for j in range(4):
        nx = c + dx[j]
        ny = r + dy[j]
        if 1 <= nx < n+1 and 1 <= ny < n+1:
            if grid[ny][nx] == 1:
                cnt += 1

    if cnt == 3:
        print(1)
    else:
        print(0)
