n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [-1, 0, 0 ,1]
dy = [0, -1, 1, 0]

start_x, start_y = 0, 0
for i in range(n):
    if dir[i] == 'W':
        for j in range(dist[i]):
            start_x += dx[0]
            start_y += dy[0]
    elif dir[i] == 'S':
        for j in range(dist[i]):
            start_x += dx[1]
            start_y += dy[1]
    elif dir[i] == 'N':
        for j in range(dist[i]):
            start_x += dx[2]
            start_y += dy[2]
    elif dir[i] == 'E':
        for j in range(dist[i]):
            start_x += dx[3]
            start_y += dy[3]
print(f'{start_x} {start_y}')