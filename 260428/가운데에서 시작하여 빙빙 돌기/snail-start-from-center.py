n = int(input())
grid = [[0] * n for _ in range(n)]
x, y = n-1, n-1
grid[y][x] = n*n
d = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(n*n-1, 0, -1):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] == 0:
        x, y = nx, ny
        grid[y][x] = i
    else:
        d = (d + 1) % 4
        x += dx[d]
        y += dy[d]
        grid[y][x] = i
for i in grid:
    print(*i)
