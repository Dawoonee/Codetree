n = int(input())
grid = [list('.'+ input()+'.') for _ in range(n)]
k = int(input())-1
grid = [['.']*(n+2)] + grid + [['.']*(n+2)]
x, y = 1, 1
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0
for i in range(k):
    x += dx[d]
    y += dy[d]
    if 0 <= x < n and 0 <= y < n:
        continue
    else:
        d += 1
        if d > 3:
            d = 0
visited = [[False]*(n+2) for _ in range(n+2)]
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if grid[ny][nx] == '.':
        visited[ny][nx] = True
        break
d = i

d += 1
if d >3:
    d -= 3
cnt = 0
while True:
    if grid[y][x] == '.':
        break
    visited[y][x] = True
    if grid[y][x] == '\\':
        d = d^1
    elif grid[y][x] == '/':
        d = d^3
    x += dx[d]
    y += dy[d]
    cnt += 1
print(cnt)
