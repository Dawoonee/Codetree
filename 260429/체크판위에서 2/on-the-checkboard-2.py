from collections import deque
R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

x, y = 0, 0
state = grid[y][x]
Q = deque([(x, y, state, 0)])
a = 0
while Q:
    x, y, state, cnt = Q.popleft()
    if x == C-1 and y == R-1 and cnt-1 == 2:
        a += 1
    for i in range(y+1, R):
        for j in range(x+1, C):
            if state != grid[i][j] and cnt <= 2:
                Q.append((j, i, grid[i][j], cnt+1))

print(a)