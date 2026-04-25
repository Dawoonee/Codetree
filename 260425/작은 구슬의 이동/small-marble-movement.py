n, t = map(int, input().split())
y, x, d = input().split()
y, x = int(y), int(x)

if d == 'U':
    d = 0
elif d == 'D':
    d = 1
elif d == 'R':
    d = 2
elif d == 'L':
    d = 3

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(t):
    # print(x, y)
    x += dx[d]
    y += dy[d]
    if x < 1:
        x = 1
        d = 2
    if y < 1:
        y = 1
        d = 1
    if x > n:
        x = n
        d = 3
    if y > n:
        y = n
        d = 0
print(f'{y} {x}')