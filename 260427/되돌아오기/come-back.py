N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
x, y = 0, 0
time = 0
for i in range(N):
    if dir[i] == 'W':
        d = 0
    elif dir[i] == 'S':
        d = 1
    elif dir[i] == 'N':
        d = 2
    elif dir[i] == 'E':
        d = 3
    
    for j in range(dist[i]):
        x += dx[d]
        y += dy[d]
        time += 1
        if x == 0 and y == 0:
            exit(print(time))
print(-1)