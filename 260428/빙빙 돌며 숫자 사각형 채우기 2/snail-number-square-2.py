n, m = map(int, input().split())

grid = [[0]*m for _ in range(n)]
grid[0][0] = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0
x, y = 0, 0
for i in range(2, n*m+1):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] == 0:
        x, y = nx, ny
        grid[y][x] = i
    else:
        d = (d+1)%4
        x += dx[d]
        y += dy[d]
        grid[y][x] = i
for i in grid:
    print(*i)

# Please write your code here.