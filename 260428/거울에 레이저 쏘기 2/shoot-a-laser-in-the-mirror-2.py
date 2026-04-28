n = int(input())
grid = [list('.' + input().strip() + '.') for _ in range(n)]
k = int(input()) - 1
grid = [['.'] * (n + 2)] + grid + [['.'] * (n + 2)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x, y = 1, 1
d = 0
for _ in range(k):
    nx = x + dx[d]
    ny = y + dy[d]
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny
    else:
        d = (d + 1) % 4
        x += dx[d]
        y += dy[d]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if grid[ny][nx] == '.':
        d = (i + 2) % 4
        break

cnt = 0
while True:
    if grid[y][x] == '.':
        break

    if grid[y][x] == '\\':
        d = d ^ 1
    elif grid[y][x] == '/':
        d = d ^ 3

    x += dx[d]
    y += dy[d]
    cnt += 1

print(cnt)