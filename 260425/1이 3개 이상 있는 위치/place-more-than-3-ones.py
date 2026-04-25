n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
sum_cnt = 0
for y in range(n):
    for x in range(n):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if grid[ny][nx] == 1:
                    cnt += 1
        if cnt >= 3:
            sum_cnt += 1
print(sum_cnt)