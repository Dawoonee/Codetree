n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_c = 0
for y in range(n):
    for x in range(n):
        c = 0
        for i in range(x, x+3):
            if i < n:
                c += grid[y][i]
        max_c = max(c, max_c)
print(max_c)