n, m = map(int, input().split())

grid = [[0]*m for _ in range(n)]
cp = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 23:'V', 24:'W', 25:'X', 26:'Y', 27:'Z'}
grid[0][0] = cp[1]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0
x, y = 0, 0
for i in range(2, n*m+1):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] == 0:
        x, y = nx, ny
        grid[y][x] = cp[i]
    else:
        d = (d+1)%4
        x += dx[d]
        y += dy[d]
        grid[y][x] = cp[i]
for i in grid:
    print(*i)

