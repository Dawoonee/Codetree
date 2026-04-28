N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
l = []
d = 0
x, y = N//2, N//2
l.append(board[y][x])
for c in str:
    if c == 'R':
        d = (d+1)%4
    elif c == 'L':
        d = (d-1)%4
    elif c == 'F':
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
            l.append(board[y][x])
print(sum(l))