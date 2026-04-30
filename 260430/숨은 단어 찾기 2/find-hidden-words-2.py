N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]
start = []
cnt = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] != 'L':
            continue
        else:
            start.append((x, y))
def dfs(x, y, s ,depth, state):
    global cnt
    if s == 'LEE':
        cnt += 1
        return
    if depth > 3:
        return
    nx = x + dx[state]
    ny = y + dy[state]
    if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
        visited[ny][nx] = True
        dfs(nx, ny, s+arr[ny][nx], depth + 1, state)
        visited[ny][nx] = False

    return
for x, y in start:
    for i in range(8):
        visited[y][x] = True
        dfs(x, y, 'L', 0, i)
        visited[y][x] = False
print(cnt)
