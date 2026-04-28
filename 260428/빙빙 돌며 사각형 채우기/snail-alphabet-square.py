n, m = map(int, input().split())

grid = [[0]*m for _ in range(n)]
cp = {
    0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z',
}
grid[0][0] = cp[0]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = 0
x, y = 0, 0
for i in range(1, n*m):
    nx = x + dx[d]
    ny = y + dy[d]
    i = i%26
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